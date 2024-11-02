from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    return HttpResponse('This is our BLOG page. :P')

def blog_second(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    return HttpResponse('This is our second BLOG page. :P')