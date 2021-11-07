from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,  login
from .models import Profile
# Create your views here.
def register(request):
    if(request.method == 'POST'):
        firstname = request.POST['firstN']
        lastname = request.POST['lastN']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        user = User.objects.create_user(username, '',password)
        user.firstN = firstname
        user.lastN = lastname
        user.save()
        password = hash(password)
        password1 = hash(password1)
      
        profile = Profile(firstN=firstname,lastN=lastname,username=username,email=email,password=password,password1=password1)
        profile.save()
        return render(request, 'register/que_page.html',{'username':username})
    return render(request,'register/register.html')

    
     
    
   
 



def Logins(request):
  if request.method=="post":
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      return render(request,'register/que_page.html',{'username':username})
    else:
      return render(request,'register/login.html')
  return render(request,'register/login.html')
@login_required(login_url=None)


def que(request):
  
  return render(request,'register/que_page.html')

      
       
  

  




