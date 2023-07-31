from django.db import models
from property.models import Property
from tenant.models import Tenant

class Unit(models.Model):
    STATUS_CHOICES = (
        ('V', 'VACANT'),
        ('O', 'OCCUPIED'),
        ('U', 'UNDER MAINTENANCE')
    )
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default='V')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, default = None)
    tenant = models.ForeignKey(
        Tenant, 
        models.SET_NULL,
        blank = True,
        null = True,
        )
    
