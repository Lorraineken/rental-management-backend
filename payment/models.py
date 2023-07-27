from django.db import models

# Create your models here.
class Payment(models.Model):
    method = models.CharField(max_length=50)
    rent_paid = models.IntegerField()
    rent_unpaid = models.IntegerField()
    #tenant_id