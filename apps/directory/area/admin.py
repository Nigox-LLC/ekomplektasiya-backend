from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Region, District


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'prefix',
        'is_active',
        'created_at',
    )
    list_filter = (
        'is_active',
        'created_at',
    )
    search_fields = (
        'name',
        'prefix',
    )
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(District)
class DistrictAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'region',
        'is_active',
        'created_at',
    )
    list_filter = (
        'region',
        'is_active',
    )
    search_fields = (
        'name',
        'region__name',
    )
    autocomplete_fields = ('region',)
    ordering = ('region', 'name')
    readonly_fields = ('created_at', 'updated_at')
