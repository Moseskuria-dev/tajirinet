from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from auth_purchase.models import Plan
from django.contrib.auth.decorators import user_passes_test


#from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')  # Ensure the template path matches your structure

def our_services(request):
    plans = Plan.objects.all()  # Get all plans from the database
    return render(request, 'our-services.html', {'plans': plans})

def our_company(request):
    return render(request, 'our-company.html')

def contact(request):
    return render(request, 'contact.html')
from django.utils import timezone  # Import timezone for getting the current time

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")
        email = data.get("email")
        name = data.get("name")  # Get the name from the data

        # Get the current date and time
        current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        # Define the recipients
        recipients = ['moseswriter01@gmail.com', 'robert.wamwea2015@gmail.com']

        # Create the email body with the user's name, email, current date/time, and message
        email_body = f"Message from {name} <{email}>\n\n"
        email_body += f"Sent on: {current_time}\n\n"
        email_body += f"Message:\n{message}\n\n"
        email_body += f"Recipients: {', '.join(recipients)}"  # Recipients after the message

        # Send the email
        send_mail(
            'New message from tajirinet.com',
            email_body,  # Use the updated email body
            'youremailexample@gmail.com',  # From email
            recipients,  # Recipients list
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
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check if the user is staff/admin
            if user.is_staff or user.is_superuser:
                return redirect('admin/')  # Redirect to the Django admin panel if admin
            else:
                # Redirect regular users to the home page or other specified URL
                return redirect('homepage')  
        else:
            # Display an error message
            messages.error(request, 'Invalid email or password. Please try again.')
            return render(request, 'sign-in.html')
    else:
        return render(request, 'sign-in.html')

# Only allow access if the user is an admin
def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def edit_packages(request):
    if request.method == 'POST':
        # Check if the delete action is requested
        if 'delete' in request.POST:
            package_id = request.POST.get('delete')
            Plan.objects.filter(id=package_id).delete()  # Delete the package by ID

        # Iterate over all submitted plans and update their values
        else:  # This is for the update action
            for plan in Plan.objects.all():
                plan.name = request.POST.get(f'name_{plan.id}')
                plan.price = request.POST.get(f'price_{plan.id}')
                plan.duration = request.POST.get(f'duration_{plan.id}')
                plan.speed = request.POST.get(f'speed_{plan.id}')
                plan.installation = request.POST.get(f'installation_{plan.id}')
                plan.description = request.POST.get(f'description_{plan.id}')  # Capture description
                plan.save()

        return redirect('edit_packages')

    # Logic to retrieve packages and render the template
    plans = Plan.objects.all()
    return render(request, 'edit_packages.html', {'plans': plans})

@user_passes_test(is_admin)
def add_package(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        duration = request.POST['duration']
        speed = request.POST['speed']
        installation = request.POST['installation']
        Plan.objects.create(name=name, price=price, duration=duration, speed=speed, installation=installation)
        return redirect('edit_packages')  # Redirect to the edit packages page
    return render(request, 'add-package.html')  # Create a form for adding a package

