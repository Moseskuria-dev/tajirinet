from django.urls import path
from . import views

urlpatterns = [
    path('choose-package/', views.choose_package, name='choose-package'),
    path('purchasing-page/', views.purchasing_page, name='purchasing_page'),
    path('confirm-purchase/', views.confirm_purchase, name='confirm_purchase'),
    #path('purchase-success/', views.purchase_success, name='purchase_success'),
    #path('initiate-payment/', views.lipa_na_mpesa_online, name='lipa_na_mpesa_online'),
    #path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    #path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

    # register, confirmation, validation and callback urls
    #path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    #path('c2b/confirmation', views.confirmation, name="confirmation"),
    #path('c2b/validation', views.validation, name="validation"),
    #path('c2b/callback', views.call_back, name="call_back"),
    path('plans/', views.plans_view, name='plans'),
    ]
