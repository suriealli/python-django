from django.conf.urls import patterns,url
from django.contrib import admin
from rango import views

urlpatterns = patterns ('',
	# url(r'^$',views.first,name = 'index'),
    url(r'^first$',views.first, name='first'),
	)