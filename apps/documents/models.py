from django.db import models
from apps.deals.models import Deal

class Invoice(models.Model):
    deal = models.OneToOneField(Deal, on_delete=models.CASCADE)
    issue_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Счет для сделки {self.deal.id}"

class Waybill(models.Model):
    deal = models.OneToOneField(Deal, on_delete=models.CASCADE)
    issue_date = models.DateField()
    total_weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Накладная для сделки {self.deal.id}"

class UPD(models.Model):
    deal = models.OneToOneField(Deal, on_delete=models.CASCADE)
    issue_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"УПД для сделки {self.deal.id}"
