"""tw_django URL Configuration

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
#from django.conf.urls import url
from django.conf.urls import patterns,url
# from django.conf.urls import url
from django.conf.urls import patterns,url,include
from django.contrib import admin
from django.conf import settings

from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/first'


urlpatterns = patterns('',
	#app rango urls here
	url(r'^rango/', include('rango.urls')),
	url(r'^admin/', admin.site.urls),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    #override the default urls
    url(r'^password/change/$',
                auth_views.password_change,
                name='password_change'),
    url(r'^password/change/done/$',
                auth_views.password_change_done,
                name='password_change_done'),

	)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}), )
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
