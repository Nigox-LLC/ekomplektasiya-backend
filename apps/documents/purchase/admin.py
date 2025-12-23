from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import PurchaseTypeBank, PurchaseTypeBankItem


class PurchaseTypeBankItemInline(TabularInline):
    model = PurchaseTypeBankItem
    extra = 0
    autocomplete_fields = ('appeal_letter', 'employee')


@admin.register(PurchaseTypeBank)
class PurchaseTypeBankAdmin(ModelAdmin):
    list_display = (
        'id',
        'number',
        'purchase_type',
        'bank',
        'balance',
        'created_at'
    )
    search_fields = ('number', 'bank__name', 'purchase_type__name')
    list_filter = ('purchase_type', 'bank')
    autocomplete_fields = ('purchase_type', 'bank')
    inlines = [PurchaseTypeBankItemInline]
    readonly_fields = ('created_at', 'updated_at')
