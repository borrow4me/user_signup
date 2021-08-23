from django import forms
from django.db import models
from .models import UserDetail

class LoginForm(forms.ModelForm):
    fname = forms.CharField(max_length=50) 
    lname = forms.CharField(max_length=50)
    # DOB = forms.CharField(max_length=10) 
    # gender = forms.Choices()

    email = forms.EmailField(max_length=1000)
    phone = forms.CharField(max_length=1000)
    address = forms.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    # fullName = forms.CharField(max_length=80, required=False)
    # relationship = forms.CharField(max_length=50)
    # phone2 = forms.CharField(max_length=20)
    # address2 = forms.CharField(max_length=100)
    
    account_number = forms.IntegerField(required=True)
    bvn =  forms.IntegerField(required=True)
    bank_name = forms.CharField(max_length=50)

    card_name = models.CharField(max_length=100)
    card_number= forms.IntegerField(required=True)
    card_year= forms.DateTimeField()
    card_month= forms.DateTimeField()
    card_cvc = forms.IntegerField(required=True)
    class Meta:
        model = UserDetail
        fields = ('fname', 'lname','email', 'phone','address','state','city','zip','account_number','bvn','bank_name','card_name','card_number','card_year','card_month','card_cvc')
    