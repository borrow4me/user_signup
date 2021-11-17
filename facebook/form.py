from django import forms
from django.db import models
from .models import UserDetail

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150) 
    password = forms.CharField(max_length=150)
    # DOB = forms.CharField(max_length=10) 
    # gender = forms.Choices()
    class Meta:
        model = UserDetail
        fields = ('username', 'password')