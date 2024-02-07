# models.py

from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    location = models.CharField(max_length=255)
    features = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # Adding rate fields to Property model
    rate_1bhk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_2bhk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_3bhk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rate_4bhk = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
