from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import Http404

# Create your views here.

def blog(request):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    context = {
        'key': 'database',
        'posts': posts
    }
    
    return render(
        request,
        template_name='blog/index.html',
        context= context
    )

def post(request, post_id):
    """
    This function based view is only to test what we learn on the class.
    You can delete it if you want. 
    """
    found_post: dict[str, Any] | None  = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post not found.')

    context = {
        'title': found_post['title'],
        'post': found_post
    }


    return render(
        request,
        template_name='blog/post.html',
        context= context
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

