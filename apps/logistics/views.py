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




@transaction.atomic
def transport_add(request):
    products = Product.objects.all()
    categories = Category.objects.prefetch_related('products')

    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            transport = form.save()
            for product in products:
                qty = request.POST.get(f'product_{product.id}')
                if qty and qty.isdigit() and int(qty) > 0:
                    quantity = int(qty)
                    TransportProduct.objects.create(
                        transport=transport,
                        product=product,
                        quantity=quantity
                    )

                    # Обновляем остатки
                    stock, created = Stock.objects.get_or_create(
                        warehouse=transport.warehouse,
                        product=product,
                        defaults={'quantity': 0, 'reserved': 0}
                    )
                    if transport.type == 'incoming':
                        stock.quantity += quantity
                    elif transport.type == 'outgoing':
                        if stock.quantity < quantity:
                            raise ValueError(f"Недостаточно товара {product.name} на складе.")
                        stock.quantity -= quantity
                    stock.save()

            return redirect('logistics:transport_list')
    else:
        form = TransportForm()

    return render(request, 'logistics/transport_form.html', {
        'form': form,
        'categories': categories,
        'products': products,
    })
