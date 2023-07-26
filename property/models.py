from django.db import models

# Create your models here.
class Property(models.Model):
    address = models.TextField(max_length=500)
    description = models.TextField(max_length=1000)
    no_of_units = models.IntegerField()
    rental_price = models.IntegerField()
    #landlord = models.ForeignKey('Landlord',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.address



