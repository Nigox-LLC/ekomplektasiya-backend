from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Bank, WareHouse


@admin.register(Bank)
class BankAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'short_name',
        'mfo',
        'stir',
        'city',
        'region',
        'district',
        'is_active',
        'created_at',
    )
    search_fields = ('name', 'short_name', 'mfo', 'stir', 'city')
    list_filter = ('region', 'district', 'is_active')
    autocomplete_fields = ('region', 'district')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(WareHouse)
class WareHouseAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'region',
        'district',
        'phone',
        'is_active',
        'created_at',
    )
    search_fields = ('name', 'phone')
    list_filter = ('region', 'district', 'is_active')
    autocomplete_fields = ('region', 'district')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
