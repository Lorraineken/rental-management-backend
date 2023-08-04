from django.db import models
from landlord.models import Landlord
from tenant.models import Tenant

class Agreement(models.Model):
    lease_terms = models.JSONField()
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    landlord = models.ForeignKey(Landlord,on_delete=models.PROTECT, default = None)
    tenant = models.ForeignKey(Tenant,on_delete=models.DO_NOTHING, default = None)

    def __str__(self):
        """String for representing the Model object."""
        return (f'start_date:{self.start_date}, end_date:{self.end_date}')

