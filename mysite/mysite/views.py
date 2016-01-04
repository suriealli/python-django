#!/usr/bin/python3
#1
from django.template import Template,Context
#2
from django.template.loader import get_template
#3
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
import datetime



def hello(request):
    return HttpResponse('hello')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" %now
    return HttpResponse(html)

def current_datetime0(request):
    now = datetime.datetime.now()
    template = '<html><body>It is now {{ now }}.</body></html>'
    t = Template(template)
    html=t.render(Context({'now':now}))
    return HttpResponse(html)

def current_datetime1(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'now':now}))
    return HttpResponse(html)

def current_datetime2(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())

def hours_ahead(request,plus):
    try:
        plus = int(plus)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=plus)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (plus, dt)
    return HttpResponse(html)

def hours_ahead1(request,plus):
    try:
        plus = int(plus)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now() + datetime.timedelta(hours=plus)
    return render_to_response('hours_ahead.html',locals())
