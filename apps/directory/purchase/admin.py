from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import PurchaseType


@admin.register(PurchaseType)
class PurchaseTypeAdmin(ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
