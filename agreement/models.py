from django.db import models

class Agreement(models.Model):
    lease_terms = models.JSONField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    #landlord_id
    #tenant_id

