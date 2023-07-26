from django.db import models

class Communication(models.Model):
    message = models.TextField(max_length=1000)
    dateTime = models.DateTimeField(auto_now=False, auto_now_add=False)
    #sender_id
    #recipient_id
