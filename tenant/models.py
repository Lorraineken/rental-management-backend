from django.db import models

# Create your models here.
class Tenant(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    idPassport = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    #unit


