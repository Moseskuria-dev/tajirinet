from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')  # Ensure the template path matches your structure

def our_services(request):
    return render(request, 'our-services.html')

def our_company(request):
    return render(request, 'our-company.html')

def subscribe(request, package):
    return redirect('contact')

def contact(request):
    return render(request, 'contact.html')

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")
        email = data.get("email")
        name = data.get("name")  # Get the name from the data

        # Create the email body with the user's name and email
        email_body = f"Message from {name} <{email}>\n\n{message}"

        # Send the email
        send_mail(
            'New message from website',
            email_body,  # Use the new email body
            'youremailexample@gmail.com',  # From email
            ['moseswriter01@gmail.com'],  # To email
            fail_silently=False,
        )
        return JsonResponse({'status': 'success', 'message': 'Email sent!'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
def sign_in(request):
    return render(request, 'sign-in.html')
def sign_up(request):
    return render(request, 'sign-up.html')