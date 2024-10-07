# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),  # Map the root URL of core to the index view
    path('our-services/', views.our_services, name='our-services'),
    path('our-company/', views.our_company, name='our-company')
]
