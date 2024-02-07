# models.py

from django.db import models
from datetime import datetime, timedelta
from property.models import Property  


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.FileField(upload_to='tenant_documents/')


    def __str__(self):
        return self.name


class TenantUnit(models.Model):
    tenant_id = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    agreement_end_date = models.DateField(default= datetime.now() + timedelta(days=365))
    monthly_rent_date = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tenant_id.name}'s Unit at {self.property_id.name}"