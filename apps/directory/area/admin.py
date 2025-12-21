from django.contrib import admin
from .models import Region, District


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
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


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
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
    ordering = ('region', 'name')
