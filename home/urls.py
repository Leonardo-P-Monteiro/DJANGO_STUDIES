from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('home_second/', views.home_second),
]