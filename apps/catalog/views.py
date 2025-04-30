# catalog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from apps.warehouse.models import Stock, Warehouse




def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:category_list')  # переадресация на список категорий
    else:
        form = CategoryForm()
    return render(request, 'catalog/category_add.html', {'form': form})




def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()  # берём все товары, связанные с этой категорией
    return render(request, 'catalog/category_detail.html', {
        'category': category,
        'products': products,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    stock_data = Stock.objects.filter(product=product).select_related('warehouse')
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'stock_data': stock_data,
    })

def product_add(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.category = category
            product.save()
            return redirect('catalog:category_detail', category_id=category.id)
    else:
        form = ProductForm()

    return render(request, 'catalog/product_add.html', {'form': form, 'category': category})
