
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
     url(r'^admin/', include(admin.site.urls)),
     url(r'', include('blog.urls')),
]

from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
