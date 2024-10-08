from django.urls import path
from .views import choose_package, purchasing_page, confirm_purchase

urlpatterns = [
    path('choose-package/', choose_package, name='choose-package'),
    path('purchasing-page/', purchasing_page, name='purchasing_page'),
    path('confirm-purchase/', confirm_purchase, name='confirm_purchase'),
]
