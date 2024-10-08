from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'speed')  # Columns to display
    search_fields = ('name',)  # Allow searching by package name
