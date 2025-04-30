# catalog/urls.py
from django.urls import path
from apps.catalog.views import *

app_name = 'catalog'

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/', category_detail, name='category_detail'),
    path('category/add/', category_add, name='category_add'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('category/<int:category_id>/add/', product_add, name='product_add'),
]
