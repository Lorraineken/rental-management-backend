# from django.db import models

# class Payment(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     payment_date = models.DateField()
#     description = models.TextField()

#     def __str__(self):
#         return f"Payment #{self.pk}: {self.amount} on {self.payment_date}"


from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Payment - {self.amount} on {self.payment_date}"
