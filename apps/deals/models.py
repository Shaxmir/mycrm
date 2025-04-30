from django.db import models
from apps.users.models import User  # Подключаем модель пользователя (если нужна)
from apps.catalog.models import Product

class Deal(models.Model):
    DEAL_STATUSES = [
        ('processing', 'В обработке'),
        ('invoice_created', 'Сделан Счет/Накладная'),
        ('paid', 'Оплачено'),
        ('cutting', 'Отдано в распил'),
        ('completed', 'Сделка завершена'),
    ]

    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=DEAL_STATUSES, default='processing')
    products = models.ManyToManyField(Product, through='DealProduct')
    responsible = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Сделка с {self.client_name} (ID: {self.id})"

class DealProduct(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} — {self.quantity} шт."
