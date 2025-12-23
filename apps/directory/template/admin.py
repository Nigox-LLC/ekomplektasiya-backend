from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Template


@admin.register(Template)
class TemplateAdmin(ModelAdmin):
    list_display = ('id', 'name', 'category', 'employee', 'is_active', 'created_at')
    search_fields = ('name', 'employee__full_name', 'category__name')
    list_filter = ('category', 'is_active')
    autocomplete_fields = ('employee', 'category')
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
