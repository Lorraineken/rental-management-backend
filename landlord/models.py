from django.db import models

# Create your models here.
class Landlord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    company = models.CharField(max_length=200)
