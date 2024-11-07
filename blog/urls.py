from django.urls import path, include
from . import views

app_name = 'blog'

# blog/
urlpatterns = [
    path('', views.blog, name = 'home'),
    path('blog_second', views.blog_second, name = 'blog_second'),
    path('<int:post_id>/', views.post, name = 'post'),
]