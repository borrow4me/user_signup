from django import forms
from .models import UserDetail

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000)
    class Meta:
        model = UserDetail
        fields = ('email', 'password')
        