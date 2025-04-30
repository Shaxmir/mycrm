# apps/logistics/views.py
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Transport, TransportProduct
from apps.warehouse.models import Stock, Warehouse
from apps.catalog.models import Product
from .forms import TransportForm, TransportProductForm
from apps.catalog.models import Category
from django.db import transaction

def transport_list(request):
    transports = Transport.objects.all().order_by('-date')
    return render(request, 'logistics/transport_list.html', {'transports': transports})




def transport_add(request):
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            transport = form.save()
            products = request.POST.getlist('product')
            quantities = request.POST.getlist('quantity')

            for product_id, qty in zip(products, quantities):
                product = Product.objects.get(id=product_id)
                quantity = int(qty)

                TransportProduct.objects.create(
                    transport=transport,
                    product=product,
                    quantity=quantity
                )

                # обновляем или создаем запись о товаре на складе
                stock, created = Stock.objects.get_or_create(
                    product=product,
                    warehouse=transport.warehouse,
                    defaults={'quantity': 0, 'reserved': 0}
                )
                if transport.type == 'incoming':
                    stock.quantity += quantity
                elif transport.type == 'outgoing':
                    stock.quantity = max(stock.quantity - quantity, 0)
                stock.save()
            return redirect('transport_list')
    else:
        form = TransportForm()
    categories = Category.objects.prefetch_related('products').all()
    products = Product.objects.all()
    return render(request, 'logistics/transport_form.html', {
        'form': form,
        'products': Product.objects.all(),  # можно убрать, если больше не используется
        'categories': categories,
    })
