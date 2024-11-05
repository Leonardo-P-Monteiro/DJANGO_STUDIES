from django.shortcuts import render

# Create your views here.

def blog(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    return render(
        request,
        template_name='blog/index.html'
    )

def blog_second(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    return render(
        request,
        template_name='blog/blog_second.html'
    )