from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ProductType, ProductModel


@admin.register(ProductType)
class ProductTypeAdmin(ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ProductModel)
class ProductModelAdmin(ModelAdmin):
    list_display = ('id', 'name', 'product_type', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('product_type', 'is_active')
    ordering = ('name',)
    autocomplete_fields = ('product_type',)
    readonly_fields = ('created_at', 'updated_at')
