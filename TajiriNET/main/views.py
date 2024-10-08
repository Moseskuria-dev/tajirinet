from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
#from django.contrib.auth.models import User

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

def sign_up(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password == confirm_password:
            # Create the user with UserCreationForm
            form = UserCreationForm({
                'username': email,  # Assuming username is the email
                'password1': password,
                'password2': confirm_password,
            })

            if form.is_valid():
                # Save the user and login
                user = form.save(commit=False)
                user.first_name = full_name.split()[0]  # First name
                user.last_name = ' '.join(full_name.split()[1:])  # Last name
                user.email = email  # Set email address
                user.save()  # Save user to database
                login(request, user)  # Log in the user after sign-up
                return redirect('purchasing_page')  # Redirect to purchase page
            else:
                # Handle form errors
                messages.error(request, 'Invalid form submission. Please correct the errors.')
                return render(request, 'sign-up.html', {'form': form})
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'sign-up.html')

    # Render the sign-up form on GET request
    return render(request, 'sign-up.html', {'form': UserCreationForm()})

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)  # Log in the user

            # Get the next URL from the query parameters, if provided
            next_url = request.GET.get('next', 'homepage')  # Default redirect to purchasing_page
            return redirect(next_url)  # Redirect to the next URL or default URL
        else:
            # Invalid login credentials
            messages.error(request, 'Invalid email or password.')
            return render(request, 'sign-in.html')

    # Render sign-in form on GET request
    return render(request, 'sign-in.html')

