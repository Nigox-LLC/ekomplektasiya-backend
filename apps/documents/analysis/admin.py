from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import (
    PriceAnalysis,
    PriceAnalysisCommercial,
    PriceAnalysisItem,
    PriceAnalysisSigned,
)


class PriceAnalysisItemInline(TabularInline):
    model = PriceAnalysisItem
    extra = 0
    autocomplete_fields = ('order_product', 'commercial_item')
    fields = ('order_product', 'quantity', 'price', 'commercial_item')


class PriceAnalysisCommercialInline(TabularInline):
    model = PriceAnalysisCommercial
    extra = 0
    autocomplete_fields = ('commercial',)


@admin.register(PriceAnalysisCommercial)
class PriceAnalysisCommercialAdmin(ModelAdmin):
    list_display = ('id', 'price_analysis', 'commercial', 'created_at')
    search_fields = ('price_analysis__number', 'commercial__number')
    autocomplete_fields = ('price_analysis', 'commercial')


@admin.register(PriceAnalysis)
class PriceAnalysisAdmin(ModelAdmin):
    list_display = ('id', 'number', 'employee', 'is_active', 'created_at')
    search_fields = ('number', 'employee__full_name')
    list_filter = ('is_active',)
    autocomplete_fields = ('employee',)
    inlines = [PriceAnalysisCommercialInline, PriceAnalysisItemInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(PriceAnalysisSigned)
class PriceAnalysisSignedAdmin(ModelAdmin):
    list_display = (
        'id',
        'price_analysis',
        'employee',
        'is_approved',
        'signed_date',
        'is_active',
        'created_at',
    )
    search_fields = ('price_analysis__number', 'employee__full_name')
    list_filter = ('is_approved', 'signed_date', 'is_active')
    autocomplete_fields = ('price_analysis', 'employee')
    readonly_fields = ('created_at', 'updated_at')
