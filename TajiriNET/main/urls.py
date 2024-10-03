# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-home'),  # Map the root URL of core to the index view
]
