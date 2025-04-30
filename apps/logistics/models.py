from django.db import models
from apps.warehouse.models import Warehouse
from apps.catalog.models import Product

class Transport(models.Model):
    TRANSPORT_TYPES = [
        ('incoming', 'Приход'),
        ('outgoing', 'Расход'),
    ]
    
    type = models.CharField(max_length=50, choices=TRANSPORT_TYPES)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='TransportProduct')
    
    def __str__(self):
        return f"{self.type} на склад {self.warehouse.name}"

class TransportProduct(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} — {self.quantity} шт."
