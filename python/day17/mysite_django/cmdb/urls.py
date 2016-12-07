"""mysite_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cmdb import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^data/(?P<p1>\d+)/(?P<p2>\d+)/', views.data1),
    url(r'^data/', views.data),
    url(r'^list/(\d+)/', views.list),
    url(r'^detail/(\d+)/', views.detail),
    url(r'^template/', views.template),
    url(r'^assets/', views.assets),
    url(r'^userinfo/', views.userinfo),
    url(r'^ajax_demo/', views.ajax_demo),
    url(r'^小黄人/', views.huang),

]
