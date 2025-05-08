# apps/logistics/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Transport, TransportProduct
from apps.warehouse.models import Stock, Warehouse
from apps.catalog.models import Product
from .forms import TransportForm, TransportProductForm
from apps.catalog.models import Category, Product
from django.db import transaction
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.http import JsonResponse

@require_POST
def create_product_api(request):
    data = request.POST
    name = data.get("name")
    category_id = data.get("category")

    if not name or not category_id:
        return JsonResponse({"error": "Имя и категория обязательны"}, status=400)

    category = Category.objects.get(id=category_id)

    product = Product.objects.create(
        name=name,
        category=category,
        photo = request.FILES.get("photo"),
        thickness=data.get("thickness") or None,
        grade=data.get("grade") or None,
        format=data.get("format") or None,
        surface=data.get("surface") or None,
        emission_class=data.get("emission_class") or None,
        sheets_per_cubic_meter=data.get("sheets_per_cubic_meter") or None,
        unit=data.get("unit") or None,
        weight=data.get("weight") or None,
        area=data.get("area") or None,
        purchase_price=data.get("purchase_price") or None,
        sale_price=data.get("sale_price") or None,
        sku=data.get("sku") or None,
        barcode=data.get("barcode") or None,
        min_stock=data.get("min_stock") or None,
        note=data.get("note") or None,
    )

    return JsonResponse({
        "id": product.id,
        "name": product.name,
        "thickness": str(product.thickness or ""),
        "unit": product.unit or "",
        "format": product.format or "",
        "grade": product.grade or "",
        "surface": product.surface or "",
})




def transport_list(request):
    transports = Transport.objects.all().order_by('-date')
    return render(request, 'logistics/transport_list.html', {'transports': transports})

def transport_detail(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    products = transport.transportproduct_set.select_related('product')
    html = render_to_string('logistics/transport_detail_panel.html', {
        'transport': transport,
        'products': products
    })
    return HttpResponse(html)



def product_card_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'logistics/transport_product_card.html', {'product': product})


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
            return redirect('logistics:transport_list')
    else:
        form = TransportForm()
    # Получаем все родительские категории
    parent_categories = Category.objects.filter(is_parent=True)

    # Получаем все товары по категориям
    categories_with_products = {}
    for parent in parent_categories:
        subcategories = parent.subcategories.all()
        categories_with_products[parent] = {}
        for subcategory in subcategories:
            products = Product.objects.filter(category=subcategory)
            categories_with_products[parent][subcategory] = products
    categories = Category.objects.prefetch_related('products').all()
    products = Product.objects.all()
    return render(request, 'logistics/transport_form.html', {
        'categories_with_products': categories_with_products,
        'form': form,
        'products': Product.objects.all(),  # можно убрать, если больше не используется
        'categories': categories,
    })
