from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import AnnualPlan, AnnualPlanItem, AnnualPlanItemMonth


class AnnualPlanItemInline(TabularInline):
    model = AnnualPlanItem
    extra = 0
    show_change_link = True


class AnnualPlanItemMonthInline(TabularInline):
    model = AnnualPlanItemMonth
    extra = 0
    ordering = ('month',)


@admin.register(AnnualPlan)
class AnnualPlanAdmin(ModelAdmin):
    list_display = ('id', 'for_year', 'region', 'district', 'created_at')
    search_fields = ('for_year', 'region__name', 'district__name')
    list_filter = ('for_year', 'region', 'district')
    autocomplete_fields = ('region', 'district')
    inlines = [AnnualPlanItemInline]
    ordering = ('-for_year',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AnnualPlanItem)
class AnnualPlanItemAdmin(ModelAdmin):
    list_display = ('id', 'name', 'annual_plan', 'is_approved', 'created_at')
    search_fields = ('name', 'annual_plan__id')
    list_filter = ('is_approved', 'annual_plan__for_year')
    autocomplete_fields = ('annual_plan',)
    inlines = [AnnualPlanItemMonthInline]
    readonly_fields = ('created_at', 'updated_at')
