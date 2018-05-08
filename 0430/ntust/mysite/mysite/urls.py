from django.conf.urls import url,include
from django.contrib import admin 
urlpatterns = [
	url(r'^blog/',include('blog.urls')),
	url(r'^mothers_day/',include('mothers_day.urls')),
    url(r'^admin/', admin.site.urls),
    ]