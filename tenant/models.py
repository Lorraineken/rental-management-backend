from django.db import models


# Create your models here.
class Tenant(models.Model):
    firstName = models.CharField(max_length=30,null=False)
    lastName = models.CharField(max_length=30,null=False)
    idPassport = models.CharField(max_length=50,null=False)
    phone = models.IntegerField(null=False)
    email = models.EmailField(max_length=254)
    


