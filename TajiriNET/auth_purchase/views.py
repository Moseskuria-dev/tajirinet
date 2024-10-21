from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Plan
from django.conf import settings
import requests
import base64
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from requests.auth import HTTPBasicAuth
import json
#from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
#from .models import MpesaPayment

def plans_view(request):
    plans = Plan.objects.all()  # Fetch all plans from the database
    return render(request, 'plans.html', {'plans': plans})  # Pass plans to the template


def choose_package(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # If authenticated, redirect to the purchasing page
        return redirect('purchasing_page')
    else:
        # If not authenticated, redirect to the login page
        return redirect('sign-in')  # Make sure to use the correct URL name for the login page

@login_required  # Ensure the user is logged in
def purchasing_page(request):
    plans = Plan.objects.all()

    # Check if a plan is selected
    plan_id = request.GET.get('plan')
    selected_plan = None
    if plan_id:
        selected_plan = get_object_or_404(Plan, id=plan_id)

    context = {
        'plans': plans,
        'selected_plan': selected_plan,
    }
    
    return render(request, 'purchase_form.html', context)

@login_required  # Ensure the user is logged in
def confirm_purchase(request):
    if request.method == 'POST':
        phone = request.POST.get('phone_number')
        plan = request.POST.get('plan')
        # Handle the purchase confirmation logic here
        # For example, save the purchase to the database or send a confirmation email
        return render(request, 'purchase_success.html', {'plan': plan, 'phone': phone})

    # If not POST, render the form again
    plan = request.GET.get('plan', None)
    return render(request, 'purchase_form.html', {'plan': plan})
