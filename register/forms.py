from django import forms
from django.contrib.auth.models import User
from .models import Login, Profile

 



#class ProfileForm(forms.ModelForm):
 # password=forms.CharField(widget=forms.PasswordInput())
  #password1=forms.CharField( label='Confirm Password (again)',widget=forms.PasswordInput())
  #class Meta():
   # model=Profile
    #fields=('firstN','lastN','username','email','password','password1')

  
#class LoginForm(forms.ModelForm):
 # password_=forms.CharField(widget=forms.PasswordInput())
  #class Meta():
   # model=Login
    #fields=('username',)