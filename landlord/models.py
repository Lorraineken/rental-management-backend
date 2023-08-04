from django.db import models

# Create your models here.
class Landlord(models.Model):
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    phone_no = models.IntegerField(null=False)
    email = models.EmailField(max_length=254,null=True)
    company = models.CharField(max_length=200,null=True)

    def __str__(self):
        """String for representing the Model object."""
        return (f'{self.first_name} {self.last_name} - {self.phone_no}')


