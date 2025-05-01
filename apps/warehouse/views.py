# apps/warehouse/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Warehouse, Stock
from apps.catalog.models import Product
from django.urls import reverse
from django import forms
from .forms import StockForm


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'address']

def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouse/warehouse_list.html', {'warehouses': warehouses})

def warehouse_add(request):
    form = WarehouseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('warehouse:warehouse_list')
    return render(request, 'warehouse/warehouse_form.html', {'form': form})

def warehouse_detail(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    stocks = warehouse.stocks.select_related('product')
    return render(request, 'warehouse/warehouse_detail.html', {
        'warehouse': warehouse,
        'stocks': stocks
    })



# ################


def stock_add(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)

    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.warehouse = warehouse
            stock.save()
            return redirect(reverse('warehouse:warehouse_detail', args=[warehouse.id]))
    else:
        form = StockForm()

    return render(request, 'warehouse/stock_form.html', {'form': form, 'warehouse': warehouse})

# Вьюха для редактирования остатка
def stock_edit(request, warehouse_id, product_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    stock = get_object_or_404(Stock, warehouse=warehouse, product_id=product_id)

    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('warehouse:warehouse_detail', pk=warehouse.id)
    else:
        form = StockForm(instance=stock)

    return render(request, 'warehouse/stock_form.html', {'form': form, 'warehouse': warehouse})
