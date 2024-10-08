from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    speed = models.CharField(max_length=100)  # e.g., "100 Mbps"

    def __str__(self):
        return self.name
