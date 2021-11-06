from django.http.response import HttpResponseRedirect
from django.shortcuts import render
#from .forms import *
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate,  login
from .models import *
# Create your views here.
def register(request):
 
  if request.method=="POST":
    if request.POST.get('firstN') and request.POST.get('lastN') and request.POST.get('username') and request.POST.get('email') and request.POST.get('password') and request.POST.get('password1'):
     post=Profile()
     post.firstN=request.POST.get('firstN')
     post.lastN=request.POST.get('lastN')
     post.username=request.POST.get('username')
     post.email=request.POST.get('email')
     post.password=request.POST.get('password')
     post.password1=request.POST.get('password1')
     post.save()
     return render(request,'register/register.html')
  else:
    return render(request,'register/register.html')

    
     
    
   
 

def que(request):
  return render(request,'register/que_page.html')


def Logins(request):
  if not request.user.is_authenticated:
  

   if request.method=="post":
    if request.POST.get('username') and request.POST.get('password'):


     fm=Login()
     fm.username=request.POST.get('username')
     fm.password=request.POST.get('password')
    
     uname=fm.cleaned_data['username']
     upass=fm.cleaned_data['password']
     user = authenticate(username=uname,password=upass)
     if user is not None:
      login(request, user)
      messages.success(request,'LOGGED IN SUCCESFULLY!!!')
      return HttpResponseRedirect('/que_page/')
     else:
       messages.success(request,"The field is required")
      
     return render (request,'register/login.html')
   
      
  
      
       
  else:
     fm=Login()
  return render(request,'register/login.html')

  


