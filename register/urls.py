from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   # path('/login',views.register,name='login'),
    path('que_page/',views.que,name='que_page'),
    path('register/',views.register,name='register'),
    path('login/',views.Logins,name='login'),

]
