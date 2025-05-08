# apps/logistics/urls.py
from django.urls import path
from . import views

app_name = 'logistics'

urlpatterns = [
    path('', views.transport_list, name='transport_list'),
    path('add/', views.transport_add, name='transport_add'),
    path('transport/<int:pk>/detail/', views.transport_detail, name='transport_detail'),
    path('product/<int:pk>/card/', views.product_card_view, name='product_card'),
    path("api/create-product/", views.create_product_api, name="logistics_create_product"),
]
