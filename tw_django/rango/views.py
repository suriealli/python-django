#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Page
# Create your views here.

def first(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'rango/first_page.html', context_dict)

def second(request):
    category_list = Category.objects.order_by('-name')
    context_dict = {'categories': category_list}
    return render(request, 'rango/second_page.html', context_dict)

def third_category(request,category_name_slug): #category_name_slug这个参数必须在强制的request参数之后
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'rango/third_category.html', context_dict)

def test_first(request):
    page_list = Page.objects.order_by('title')
    context_dict = {'Pages': page_list}
    return render(request,'rango/test_first.html',context_dict)

