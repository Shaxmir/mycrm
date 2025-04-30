from django.db import models
from apps.catalog.models import Product

class Warehouse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.PositiveIntegerField(default=0)  # Кол-во на складе
    reserved = models.PositiveIntegerField(default=0)  # Кол-во в резерве

    class Meta:
        unique_together = ('product', 'warehouse')

    def available(self):
        return self.quantity - self.reserved

    def __str__(self):
        return f"{self.product.name} — {self.warehouse.name}"
