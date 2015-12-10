"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import *
from django.contrib import admin
#from django.conf.urls import *
from mysite.views import *

urlpatterns = patterns('',
	('^hello/$',hello),
	('^time0/$',current_datetime0),
	('^time1/$',current_datetime1),
	('^time2/$',current_datetime2),
	('^time/$',current_datetime),
	('^time/plus/(\d{1,2})/$',hours_ahead),
	('^time1/plus/(\d{1,2})/$',hours_ahead1),
        ('^admin/',include(admin.site.urls)),
)
