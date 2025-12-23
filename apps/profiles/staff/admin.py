from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'phone',
        'region',
        'district',
        'department',
        'position',
        'position',
        'is_active_badge',
        'created_at',
    )
    search_fields = (
        'full_name', 'phone', 'inn', 'jshshr', 
        'passport_series', 'passport_number'
    )
    list_filter = (
        'region', 'district', 'department', 
        'position', 'is_active'
    )
    autocomplete_fields = (
        'region', 'district', 'department', 'position'
    )
    ordering = ('full_name',)
    list_filter_sheet = True
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Personal Info', {
            'fields': (
                'full_name', 'birth_date', 'passport_image'
            )
        }),
        ('Passport Data', {
            'fields': (
                'passport_series', 'passport_number', 
                'jshshr', 'inn'
            )
        }),
        ('Contact Info', {
            'fields': (
                'phone', 'address', 'region', 'district'
            )
        }),
        ('Job Info', {
            'fields': (
                'department', 'position', 'warehouse'
            )
        }),
        ('Metadata', {
            'fields': (
                'is_active', 'created_at', 'updated_at'
            )
        }),
    )
    filter_horizontal = ('warehouse',)

    @display(
        description="Holati",
        ordering="is_active",
        label={
            True: "success",
            False: "danger"
        }
    )
    def is_active_badge(self, obj):
        return obj.is_active
