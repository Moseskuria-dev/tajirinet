from django.contrib import admin
from .models import Plan, MpesaPayment

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')  # Columns to display in the admin list view
    search_fields = ('name',)  # Searchable fields in the admin

admin.site.register(Plan, PlanAdmin)

admin.site.register(MpesaPayment)
