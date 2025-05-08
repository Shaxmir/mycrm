from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subcategories',  # подкатегории
        on_delete=models.CASCADE
    )
    is_parent = models.BooleanField(default=False)  # Новое поле для обозначения родительской категории

    def __str__(self):
        return self.name

    @property
    def is_root(self):
        return self.parent is None


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    thickness = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    format = models.CharField(max_length=100, null=True, blank=True)
    surface = models.CharField(max_length=100, null=True, blank=True)
    emission_class = models.CharField(max_length=50, null=True, blank=True)
    sheets_per_cubic_meter = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)
    purchase_price = models.DecimalField("Закупочная цена", max_digits=10, decimal_places=2, null=True)
    sale_price = models.DecimalField("Цена продажи", max_digits=10, decimal_places=2, null=True)
    sku = models.CharField("Артикул", max_length=100, unique=True, null=True, blank=True)
    barcode = models.CharField("Штрихкод", max_length=100, null=True, blank=True)
    vat_rate = models.DecimalField("Ставка НДС", max_digits=4, decimal_places=2, default=20.0)
    is_active = models.BooleanField("Активен", default=True)
    min_stock = models.PositiveIntegerField("Мин. остаток", null=True, blank=True)
    note = models.TextField("Примечание", null=True, blank=True)

    def __str__(self):
        return self.name
