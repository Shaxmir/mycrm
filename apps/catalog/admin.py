from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'is_parent']
    list_filter = ['is_parent']
    search_fields = ['name']
