from django.urls import path
from . import views

urlpatterns = [
    path('choose-package/', views.choose_package, name='choose-package'),
    path('purchasing-page/', views.purchasing_page, name='purchasing_page'),
    path('confirm-purchase/', views.confirm_purchase, name='confirm_purchase'),
    ]
