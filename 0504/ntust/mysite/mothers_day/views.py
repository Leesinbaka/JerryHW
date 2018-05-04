from django.shortcuts import render
from .models import *
#Create your views here.
def mother(request):
    request.method == 'POST'
    say = request.POST.get('say')
    mymum.objects.create(myword=say)
    return render(request, 'motherday.html', {'say': say})