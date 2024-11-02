from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    return HttpResponse('This is our HOMEPAGE.  :)')

def home_second(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    return HttpResponse('This is our second url of home app.  :)')