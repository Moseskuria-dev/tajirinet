from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)  # e.g., 'Monthly', 'Yearly', 'Weekly'
    speed = models.CharField(max_length=100)  # e.g., '5 Mbps Speed'
    installation = models.CharField(max_length=100, default='Free Installation')
    switches_and_routers = models.CharField(max_length=100, default='Free Switches & Routers')
    payment_method = models.CharField(max_length=100, default='Pay, Plug & Play')
    description = models.TextField()  # Add this line

    def __str__(self):
        return self.name
    
    