from django.urls import path
from .views import choose_package, purchasing_page, confirm_purchase, add_package, edit_package, package_list, manage_packages

urlpatterns = [
    path('choose-package/', choose_package, name='choose-package'),
    path('purchasing-page/', purchasing_page, name='purchasing_page'),
    path('confirm-purchase/', confirm_purchase, name='confirm_purchase'),
    path('packages/add/', add_package, name='add_package'),
    path('packages/edit/<int:pk>/', edit_package, name='edit_package'),
    path('packages/', package_list, name='package_list'),
    path('manage-packages/', manage_packages, name='manage_packages'),  

]
