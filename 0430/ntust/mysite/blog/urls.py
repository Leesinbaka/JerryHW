from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.blog, name='blog'),
	url(r'^post/', views.post, name='post'),
	url(r'^edit/', views.edit, name='edit'),
]