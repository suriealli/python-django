#coding=utf-8
from django.conf.urls import patterns,url
from django.contrib import admin
from rango import views

urlpatterns = patterns ('',
	# url(r'^$',views.first,name = 'index'),
    url(r'^first$',views.first, name='first'),
    url(r'^second$',views.second, name='second'),
    url(r'^test_first$',views.test_first, name='test_first'),
    url(r'^third_page/(?P<category_name_slug>[\w\-]+)/$', views.third_category, name='third_category'),#正则表达式会匹配URL斜杠前所有的字母数字(例如 a-z, A-Z, 或者 0-9)和连字符(-).然后把这个值作为category_name_slug参数传递给views.category()
    url(r'^fourth_add_category/$', views.fourth_add_category, name='fourth_add_category'), # 增加分类
    url(r'^fifth_add_page/(?P<category_name_slug>[\w\-]+)/$', views.fifth_add_page, name='fifth_add_page'), # 增加page
    # url(r'^register/$', views.register, name='register'), # 注册链接
    # url(r'^login/$', views.user_login, name='login'), # 登录链接
    # url(r'^logout/$', views.user_logout, name='logout'),#登出
    url(r'^restricted/', views.restricted, name='restricted'),# 权限把控
	)