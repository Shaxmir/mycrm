# apps/logistics/forms.py
from django import forms
from .models import Transport, TransportProduct
from apps.warehouse.models import Warehouse
from apps.catalog.models import Product

class TransportForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = None  # <--- Вот это убирает --------

    class Meta:
        model = Transport
        fields = ['type', 'warehouse']


class TransportProductForm(forms.ModelForm):
    class Meta:
        model = TransportProduct
        fields = ['product', 'quantity']
