# apps/logistics/urls.py
from django.urls import path
from . import views

app_name = 'logistics'

urlpatterns = [
    path('', views.transport_list, name='transport_list'),
    path('add/', views.transport_add, name='transport_add'),
]
