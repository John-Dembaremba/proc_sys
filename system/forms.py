from django import forms
from .models import Apply, Jobs

# Class

class ApplyForm(forms.ModelForm):
	zimra = forms.FileField(
            help_text = 'jpg and jpeg only'
		)
	praz = forms.FileField(
            help_text = 'jpg and jpeg only'
		)
	quotation = forms.FileField(
            help_text = 'upload qoutation form here'
		)
	class Meta:
		model = Apply
		fields = ['zimra', 'praz', 'quotation', ]


class JobsForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(
		   attrs={'rows':8, 'placeholder':'Describe Product features'}
		),
		 max_length=200)
	Request_For_Qoutation = forms.CharField(
          help_text='Insert Request For Qoutation Number'
		)
    

	class Meta:
		model = Jobs
		fields = [
		  'Request_For_Qoutation',
		  'product',
		  'description',
		  'budget',
		  'period',
  ]
 
   
