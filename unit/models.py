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
    tenant = models.OneToOneField(
        Tenant, 
        models.SET_NULL,
        blank = True,
        null = True,
        )
    
    def __str__(self):
        """String for representing the Model object."""
        return (f'status:{self.status}-tenant{self.tenant}')
