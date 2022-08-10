from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required


from .models import Product, Jobs, Apply, Profile
from django.views.generic import ListView
from .forms import JobsForm, ApplyForm
from matplotlib import image as mpimg
 
import re
import pyzbar.pyzbar as pyzbar
from datetime import datetime,  timedelta
import pandas as pd
import joblib

# Create your views here.

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'home.html'


@login_required
def Jobs_view(request, pk):
    job = get_object_or_404(Product, pk=pk)
    jobs = job.jobs.order_by('-last_update').annotate(replies=Count('supplier')) #count suppliers who applied
    close_date = timedelta(days=30)
    return render(request, 'jobs.html', {"job":job, "supply":jobs, "date":close_date})

@login_required  
def new_job_view(request, pk):
    
    job = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = JobsForm(request.POST)

        if form.is_valid:
            product = form.save(commit=False)
            product.group = job
            product.client = request.user
            product.save()
            return redirect("product_jobs", pk=job.pk)

    else:
        form = JobsForm()

    return render(request, 'new_job.html', {"form":form, "job":job})


def zimra_validity(file_path):
    img = mpimg.imread(file_path)
    try:
        decodeObject = pyzbar.decode(img)  #pyzbar decode qrcode
        for obj in decodeObject:
                data = str(obj.data) #get the decoded object and convert to string
        string_data = data.replace(":", "")
        string = string_data
        match_obj = re.search("Validity(.*) Verification", string) #capture all string between Validity and Verification
        data_str = match_obj.group(1) #return start date and end date
        split_str = data_str.rsplit() 
        end_date = split_str.pop(2) #remove start date leaving end date
  
        try:
            
            split_date_list= end_date.split('/')
            current_date = datetime.now()
            current_date_format = current_date.strftime("%m/%d/%Y")
            split_currentdate_list = current_date_format.split('/')
            '''
            compare list elements of split_date and split_currentdate get valid date 
            ''' 
            if int(split_date_list[0]>=split_currentdate_list[0])==True and int(split_date_list[2]>=split_currentdate_list[2])==True:
                if int(split_date_list[1]>=split_currentdate_list[1])==True:
                    valid = '{} valid'.format(end_date)
                    return valid
            else:
                not_valid = '{} invalid'.format(end_date)
                return not_valid
        except ValueError:
            pass
    except UnboundLocalError:
        no_qr = 'No_QRCODE'.format(decodeObject)
        print(no_qr)

def dataframe_zimra(file):
    try:
        if file.endswith("invalid"):
            dict_zimra = {"Zimra(ITF263)":[2]}
            df = pd.DataFrame(dict_zimra)
            return df
        elif file.endswith("valid"):
            dict_zimra = {"Zimra(ITF263)":[0]}
            df = pd.DataFrame(dict_zimra)
            return df
    except AttributeError:
        dict_zimra = {"Zimra(ITF263)":[1]}
        df = pd.DataFrame(dict_zimra)
        return df

def praz_validity(file_path):
    img = mpimg.imread(file_path)
    try:
        decodeObject = pyzbar.decode(img)
        for obj in decodeObject:
            data = str(obj.data)
        date_str = data.rsplit('-')
        date = date_str.pop(1)
        try:
           # date_format = datetime.strptime(date, '%Y')
            current_date = datetime.now().strftime("%Y")
            if int(date>=current_date)==True:
                valid = '{} valid'.format(date)
                return valid
            else:
                not_valid = '{} invalid'.format(date)
                return not_valid
        except ValueError:
            pass

    except UnboundLocalError:
        no_qr = 'No_QRCode'.format(decodeObject)
        return no_qr

def dataframe_praz(file):
    if file.endswith("valid"):
        dict_praz = {"PRAZ":[0]}
        df = pd.DataFrame(dict_praz)
        return df
    elif file.endswith("invalid"):
        dict_praz = {"PRAZ":[2]}
        df = pd.DataFrame(dict_praz)
        return df
    else:
        dict_praz = {"PRAZ":[1]}
        df = pd.DataFrame(dict_praz)
        return df

def prediction(zimra_file_path, praz_file_path):
    df1 = dataframe_zimra(zimra_validity(zimra_file_path))
    df2 = dataframe_praz(praz_validity(praz_file_path))
    result = pd.concat([df1, df2], axis=1)
    load_model = joblib.load(r"/home/jd/Django/proc_sys/system/DTree_Model.pkl") #load trained model
    pred = load_model.predict(result)
    if pred == 0:
        doc = "Invalid Documents"
    else:
        doc = "Valid Documents"
    return doc


@login_required
def Apply_job_view(request, pk, post_pk):
    IMAGE_FILE_TYPES = ['jpg', 'jpeg', 'png']
    apply_job = get_object_or_404(Jobs, group__pk=pk, pk=post_pk)#group__pk gets the group id 
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES) #request.Files returns files in filesystemStorage and in template it assocciate with enctype varible without it will return empty
        if form.is_valid():
            form = form.save(commit=False)
            form.suppliers = request.user # get the logged in user
            form.jobs = apply_job #get Job on product table which is foreign key from Jobs
            form.clients = apply_job.client #get client id in Jobs model on client table who post the job
            form.zimra = request.FILES['zimra']
            '''
               Accepting only formats in IMAGE_FILE_TYPES for decoding qrcode
            '''
            file = form.zimra.url.split('.')[-1]
            file.lower()
            if file not in IMAGE_FILE_TYPES:
                return render(request, 'error.html', {"apply":apply_job})
            file_zimra = form.zimra.path
            form.zimra_date = zimra_validity(form.zimra)
            
            form.praz = request.FILES['praz']
            file_ = form.praz.url.split('.')[-1]
            file_.lower()
            if file_ not in IMAGE_FILE_TYPES:
                return render(request, 'error.html', {"apply":apply_job})
            file_praz = form.praz.path
            form.praz_date = praz_validity(form.praz)
            
            form.doc_validity = prediction(form.zimra, form.praz)
            form.save()
            return redirect('product_jobs', pk=pk)

    else:
        form = ApplyForm()

    return render(request, 'apply_job.html', {"apply":apply_job, "form":form})

@login_required
def Decision_view(request, pk, post_pk):
    dec = get_object_or_404(Jobs, group__pk=pk, pk=post_pk)
    test = Apply.objects.filter(jobs__product=dec).filter(jobs_id=dec.pk).order_by('doc_validity')
    
    return render(request, 'decision.html', {"dec":dec, "apply":test})

@login_required
def chat_view(request, pk):
    chat = get_object_or_404(Profile, pk=pk)
    name = Profile.objects.filter(user_id=chat.pk)
    

    return render(request, 'chat.html', {"profile":chat, "name":name})




