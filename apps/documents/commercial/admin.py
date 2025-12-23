from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Commercial


@admin.register(Commercial)
class CommercialAdmin(ModelAdmin):
    list_display = (
        'id',
        'number',
        'date',
        'organization',
        'employee',
        'created_at',
    )
    search_fields = ('number', 'organization', 'employee__full_name')
    list_filter = ('date', 'employee')
    autocomplete_fields = ('employee', 'delivery_condition')
    date_hierarchy = 'date'
    ordering = ('-date',)
    readonly_fields = ('created_at', 'updated_at')
