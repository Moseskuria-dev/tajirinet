from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    plan = request.GET.get('plan', None)  # Get the plan from the query parameters

    return render(request, 'purchase_form.html', {'plan': plan})

@login_required  # Ensure the user is logged in
def confirm_purchase(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        plan = request.POST.get('plan')
        # Handle the purchase confirmation logic here
        # For example, save the purchase to the database or send a confirmation email
        return render(request, 'purchase_success.html', {'plan': plan, 'phone': phone})

    # If not POST, render the form again
    plan = request.GET.get('plan', None)
    return render(request, 'purchase_form.html', {'plan': plan})
