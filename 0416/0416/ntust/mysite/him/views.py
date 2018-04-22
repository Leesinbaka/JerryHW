from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.
from .models import myself
#Create your views here.
def index(request):
    me = myself.objects.all()
    return render_to_response('him/menu.html',locals())