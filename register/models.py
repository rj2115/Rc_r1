from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
# Create your models here.
class Profile(models.Model):
  
  firstN=models.CharField(max_length=30,default="")
  lastN=models.CharField(max_length=30,default="")
  username=models.CharField(max_length=30,default="")
  email=models.EmailField(max_length=30,default="")
  password=models.CharField(max_length=30,default="")
  password1=models.CharField(max_length=30,default="")


  def __str__(self):
    return self.username
class Login(models.Model):
  username=models.CharField(max_length=30)
  password=models.CharField(max_length=8)