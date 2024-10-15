from django.contrib import admin
from .models import Plan

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'speed', 'installation', 'switches_and_routers', 'payment_method', 'description')  # Include description
    search_fields = ('name',)

admin.site.register(Plan, PlanAdmin)
