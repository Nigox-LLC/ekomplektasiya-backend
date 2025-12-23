from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Unit, Size


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Unit)
class UnitAdmin(ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Size)
class SizeAdmin(ModelAdmin):
    list_display = ('id', 'name', 'product_model', 'is_active', 'created_at')
    search_fields = ('name', 'product_model__name')
    list_filter = ('product_model', 'is_active')
    autocomplete_fields = ('product_model',)
    ordering = ('product_model', 'name')
    readonly_fields = ('created_at', 'updated_at')
