from django.db import models

class Unit(models.Model):
    status = models.CharField(max_length=50)
    #property
    #tenant
    
