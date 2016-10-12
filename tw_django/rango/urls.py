#coding=utf-8
from django.conf.urls import patterns,url
from django.contrib import admin
from rango import views

urlpatterns = patterns ('',
	# url(r'^$',views.first,name = 'index'),
    url(r'^first$',views.first, name='first'),
    url(r'^second$',views.second, name='second'),
    url(r'^test_first$',views.test_first, name='test_first'),
    url(r'^third_category/(?P<category_name_slug>[\w\-]+)/$', views.third_category, name='third_category'),#正则表达式会匹配URL斜杠前所有的字母数字(例如 a-z, A-Z, 或者 0-9)和连字符(-).然后把这个值作为category_name_slug参数传递给views.category()
	)