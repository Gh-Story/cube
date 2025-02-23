"""cube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^indexPlus/solvePlus/$', solve_plus),
    url(r'^indexPlus/$', index_plus),
    url(r'^indexPlus/initState/$', initState),
    
    url(r'^index/$', index),
    url(r'^index/guidance/$', guidance),
    url(r'^index/guidance/initState/$', initState),
    url(r'^index/guidance/solvePlus/$', solve_plus),
    url(r'^index/challenge/$', challenge),
    url(r'^index/challenge/initState/$', initState),
    url(r'^index/challenge/solvePlus/$', solve_plus),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
