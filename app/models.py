from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified  = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UserDetail(BaseModel):
    email = models.EmailField(max_length=1000)
    password = models.CharField(max_length=1000)

