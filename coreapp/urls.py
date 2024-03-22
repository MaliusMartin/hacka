# coreapp/urls.py

from django.urls import path
from .views import  Home, predict_view# Import your views here

urlpatterns = [
    path('', Home, name='home'),
    path('input/', predict_view, name='input'),
    # Define other URL patterns as needed
]
