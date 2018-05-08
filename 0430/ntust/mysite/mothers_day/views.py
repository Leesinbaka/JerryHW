from django.shortcuts import render
from .models import myword
# Create your views here.
def mother(request):
	request.method == 'POST'
	say = request.POST.get('say')
	myword.objects.create(myword=say)
	return render(request,"mother.html",{'say':say})
