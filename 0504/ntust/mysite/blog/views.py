from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    request.method == 'POST'
    post = request.POST.get('post')
    Post.objects.create(text=post)
    return render(request, 'post_list.html',{'post':post})
def postdate(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('pblished_date')
    return render(request, 'post_list.html',{'posts':posts})