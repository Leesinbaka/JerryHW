from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
    url(r'^admin/', admin.site.urls),
    url(r'^changhua/',views.changhua),
]