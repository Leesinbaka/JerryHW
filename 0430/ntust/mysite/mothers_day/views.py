from django.shortcuts import render
from .models import myword
# Create your views here.
def mother(request):
	if request.method == 'POST':
		say = request.POST.get('say')
		myword.objects.create(myword=say)
		return render(request,"motherday.html",{'say':say})
	return render(request,"motherday.html")
