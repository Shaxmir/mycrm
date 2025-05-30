# apps/warehouse/forms.py
from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'warehouse', 'quantity', 'reserved']
