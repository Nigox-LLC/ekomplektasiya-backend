from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Department, Position


@admin.register(Department)
class DepartmentAdmin(ModelAdmin):
    list_display = ('id', 'name', 'index_number', 'is_active', 'created_at')
    search_fields = ('name', 'index_number')
    list_filter = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Position)
class PositionAdmin(ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
