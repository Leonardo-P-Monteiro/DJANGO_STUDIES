from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.blog),
    path('blog_second', views.blog_second),
]