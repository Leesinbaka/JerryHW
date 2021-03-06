from django.shortcuts import render ,redirect,HttpResponse
from django.contrib import auth
from .models import restaurant
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
                message='sucess'
                return redirect('/closerice/index/')
            else:
                message='nothing here'
        else:
            message='failed'
    return render(request,"login.html",locals())

# def index(request):
#     haha = restaurant.objects.all()
#     return render(request,"index.html",{'haha': haha})
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

def taipei_1(request):
    return render(request,"taipei_1.html")

def haha(request):
    rest = restaurant.objects.all()
    return render(request,"haha.html",{"rest":rest})