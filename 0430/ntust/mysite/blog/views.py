from django.shortcuts import render , redirect, get_object_or_404
from .models import post123
# Create your views here.
def blog(request):
	post_list = post123.objects.all()
	if request.method == 'POST':
		pk = request.POST.get('pk')
		get_object_or_404(post123,pk=pk).delete()
	return render(request, 'blog.html', {'post_list': post_list})

def post(request):
	request.method='POST'
	title = request.POST.get('title')
	content = request.POST.get('content')
	post123.objects.create(title=title,content=content)
	return render(request,'post.html')

def edit(request):
	pk = request.GET.get('q')
	post = get_object_or_404(post123,pk=pk)
	if request.method == 'POST':
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()
		return redirect('/blog')
	return render(request, 'edit.html', {'post': post})