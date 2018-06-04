from django.shortcuts import render_to_response ,HttpResponseRedirect
from django.contrib import auth
from .models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    # 	if request.method == 'POST':
	# 	demo = request.POST.get('demo')
	# 	return render(request,"index.html")
	# return render(request,"index.html")
    return render_to_response('index.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return HttpResponseRedirect('home')
    else:
        form = UserCreationForm()
    return render_to_response(request, 'signup.html', {'form': form})