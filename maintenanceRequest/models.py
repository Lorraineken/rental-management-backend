from django.db import models

# Create your models here.
class MaintenanceRequest(models.Model):
    description = models.TextField(max_length=1000)
    photos = models.JSONField()
    status = models.CharField(max_length=50)
    cost = models.IntegerField()
    date_time = models.DateTimeField()
    #unit_id