from django.shortcuts import render ,redirect,HttpResponse
from django.contrib import auth
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
def login(request):
    if request.method =='POST':
        name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/closerice/index/')
                message='sucess'
            else:
                message='nothing here'
        else:
            message='failed'
    return render(request,"login.html",locals())

def index(request):
    return render(request,"index.html",locals())

def logout(request):
    auth.logout(request)
    return redirect('/closerice/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/closerice/login/')
    else:
        form = UserCreationForm()
    return render(request,"register.html",locals())

def changhua(request):
    return render(request,"changhua.html")