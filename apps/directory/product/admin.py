from django.contrib import admin
from .models import ProductType, ProductModel


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_type', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('product_type',)
    ordering = ('name',)
    autocomplete_fields = ('product_type',)
