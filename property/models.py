from django.db import models
from landlord.models import Landlord

# Create your models here.
class Property(models.Model):
    address = models.TextField(max_length=500,null=False)
    description = models.TextField(max_length=1000)
    no_of_units = models.IntegerField(null=False)
    rental_price = models.IntegerField(null=False)
    landlord = models.ForeignKey(Landlord,on_delete=models.SET_NULL, null=True)
    #Add image

    def __str__(self):
        """String for representing the Model object."""
        return (f'{self.no_of_units} units, {self.rental_price} Ksh per unit')



