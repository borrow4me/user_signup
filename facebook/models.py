from django.db import models
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
    username = models.CharField(max_length=150, default='username  ') 
    password = models.CharField(max_length=150, default='password ')
