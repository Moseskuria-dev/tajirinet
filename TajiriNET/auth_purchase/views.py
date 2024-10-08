from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Package  # Make sure to import your Package model
from .forms import PackageForm  # Import the PackageForm you created

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

# New Views for Managing Packages

@login_required
def add_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the package to the database
            return redirect('package_list')  # Redirect to the package list view after saving
    else:
        form = PackageForm()
    return render(request, 'add_package.html', {'form': form})

@login_required
def edit_package(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)
        if form.is_valid():
            form.save()  # Save the updated package
            return redirect('package_list')  # Redirect to the package list view after saving
    else:
        form = PackageForm(instance=package)
    return render(request, 'edit_package.html', {'form': form, 'package': package})

@login_required
def package_list(request):
    packages = Package.objects.all()  # Retrieve all packages
    return render(request, 'package_list.html', {'packages': packages})

@login_required  # Ensure the user is logged in (Admin in this case)
def manage_packages(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new or updated package
            return redirect('manage-packages')  # Redirect to the same page after saving
    else:
        form = PackageForm()  # Initialize an empty form for GET requests

    packages = Package.objects.all()  # Fetch all packages to display
    return render(request, 'manage_packages.html', {'form': form, 'packages': packages})