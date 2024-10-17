# core/urls.py

from django.urls import path
from . import views
from .views import send_message
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='homepage'),  # Map the root URL of core to the index view
    path('our-services/', views.our_services, name='our-services'),
    path('our-company/', views.our_company, name='our-company'),
    path('contact/', views.contact, name='contact'),
    path('send-message/', send_message, name='send_message'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='sign-out'),
    path('edit-packages/', views.edit_packages, name='edit_packages'),
    path('add-package/', views.add_package, name='add_package'),
    path('homepage/', views.index, name='index'),
]

