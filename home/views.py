from django.shortcuts import render


# Create your views here.

def home(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    return render(
        request,
        template_name='home/index.html'
    )