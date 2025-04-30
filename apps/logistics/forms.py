# apps/logistics/forms.py
from django import forms
from .models import Transport, TransportProduct
from apps.warehouse.models import Warehouse
from apps.catalog.models import Product

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ['type', 'warehouse']  # Тип операции (приход/расход) и склад

class TransportProductForm(forms.ModelForm):
    class Meta:
        model = TransportProduct
        fields = ['product', 'quantity']
