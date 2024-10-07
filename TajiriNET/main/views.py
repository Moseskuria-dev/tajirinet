# core/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Ensure the template path matches your structure

def our_services(request):
    return render(request, 'our-services.html')

def our_company(request):
    return render(request, 'our-company.html')