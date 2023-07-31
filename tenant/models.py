from django.db import models


# Create your models here.
class Tenant(models.Model):
    first_name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=30,null=False)
    id_passport = models.CharField(max_length=50,null=False)
    phone_no = models.IntegerField(null=False)
    email = models.EmailField(max_length=254)
    


