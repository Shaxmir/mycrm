# apps/warehouse/urls.py
from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.warehouse_list, name='warehouse_list'),
    path('add/', views.warehouse_add, name='warehouse_add'),
    path('<int:pk>/', views.warehouse_detail, name='warehouse_detail'),
    path('<int:warehouse_id>/stocks/add/', views.stock_add, name='stock_add'),  # Добавление остатка
    path('<int:warehouse_id>/stocks/<int:stock_id>/edit/', views.stock_edit, name='stock_edit'),  # Редактирование остатка
    path('stock/<int:warehouse_id>/edit/<int:product_id>/', views.stock_edit, name='stock_edit'),  # Новый путь для редактирования
]
