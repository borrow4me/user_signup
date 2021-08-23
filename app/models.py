from typing import Optional
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, DateTimeField
import datetime

# Create your models here.

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified  = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserDetail(BaseModel):
    fname = models.CharField(max_length=50, default='first name  ') 
    lname = models.CharField(max_length=50, default='last name ')


    email = models.EmailField(max_length=1000, default='example@gmail.com ')
    phone = models.CharField(max_length=1000, default='90334587654')
    address = models.CharField(max_length=100, default='no 11 resfgt r ')
    state = models.CharField(max_length=50 , default='Lagos ')
    city = models.CharField(max_length=50 , default='lekki ')
    zip = models.CharField(max_length=50 , default='123456 ')

    # fullName = models.CharField(max_length=80, default='full name ')
    # relationship = models.CharField(max_length=50, default='sis/bro/dad')
    # phone2 = models.CharField(max_length=30, default='03045432')
    # address2 = models.CharField(max_length=100, default='no 22 2223i')
    
    account_number = models.IntegerField(default=1234567890)
    bvn =  models.IntegerField(default=2345678765)
    bank_name = models.CharField(max_length=50, default='my bsnk nsmr ')

    card_name = models.CharField(max_length=100, default='card name')
    card_number= models.IntegerField(default=456789999, max_length=40)
    card_year = models.DateTimeField(default=datetime.date.today(), null=True, blank=True)
    # card_year= models.CharField(max_length=50,default="2020")
    card_month= models.DateTimeField(default=datetime.date.today())
    card_cvc = models.IntegerField(default=000, max_length=20)
     


