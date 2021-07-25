from typing import Optional
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified  = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserDetail(BaseModel):
    fname = models.CharField(max_length=50) 
    lname = models.CharField(max_length=50)
    DOB = models.DateField(blank=True)
    # gender = models.Choices()

    email = models.EmailField(max_length=1000)
    phone = models.CharField(max_length=1000)
    address1 = models.TextField(max_length=100)

    fullName = models.CharField(max_length=80)
    relationship = models.CharField(max_length=50)
    phone2 = models.IntegerField(max_length=20)
    address2 = models.CharField(max_length=100)
    
    account_number = models.IntegerField(max_length=30)
    bvn =  models.IntegerField(max_length=30)
    bank_name = models.CharField(max_length=50)

    card_number= models.IntegerField(max_length=40)
    card_year= models.IntegerField(max_length=20)
    card_month= models.CharField(max_length=20)
    card_cvc = models.IntegerField(max_length=10)
     


