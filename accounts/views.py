#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from .forms import SignUpForm, UpdateForm, UpdateFormUserProfile
from django.db import transaction

# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()        

    return render(request, 'signup.html', {"form":form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        user_form = UpdateForm(request.POST, instance=request.user)
        profile_form = UpdateFormUserProfile(request.POST, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('home')
 

    else:
        user_form = UpdateForm(instance=request.user)
        profile_form = UpdateFormUserProfile(instance=request.user.profile)

    return render(request, 'my_account.html', {"user_form":user_form, "profile_form":profile_form})
