#!/usr/bin/python3

from django.http import HttpResponse


def hello(request):
    return HttpResponse('hello')
