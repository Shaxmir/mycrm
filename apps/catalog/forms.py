# catalog/forms.py
from django import forms
from .models import Product,Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'thickness', 'grade', 'format', 'surface', 'emission_class', 'sheets_per_cubic_meter', 'unit', 'weight', 'area', 'photo']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parent']