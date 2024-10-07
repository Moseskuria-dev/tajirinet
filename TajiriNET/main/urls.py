# core/urls.py

from django.urls import path
from . import views
from .views import send_message

urlpatterns = [
    path('', views.index, name='homepage'),  # Map the root URL of core to the index view
    path('our-services/', views.our_services, name='our-services'),
    path('our-company/', views.our_company, name='our-company'),
    path('subscribe/<str:package>/', views.subscribe, name='subscribe'),
    path('contact/', views.contact, name='contact'),
    path('send-message/', send_message, name='send_message'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    
    
]
