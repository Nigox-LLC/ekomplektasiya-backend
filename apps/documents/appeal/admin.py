from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import AppealLetter, AppealLetterItem, AppealLetterSigned


class AppealLetterItemInline(TabularInline):
    model = AppealLetterItem
    extra = 0
    autocomplete_fields = ('price_analysis',)


@admin.register(AppealLetter)
class AppealLetterAdmin(ModelAdmin):
    list_display = (
        'id',
        'number',
        'employee',
        'is_approved',
        'is_active',
        'created_at'
    )
    search_fields = ('number', 'employee__full_name')
    list_filter = ('is_approved', 'is_active')
    autocomplete_fields = ('employee',)
    inlines = [AppealLetterItemInline]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AppealLetterSigned)
class AppealLetterSignedAdmin(ModelAdmin):
    list_display = (
        'id',
        'appeal_letter',
        'price_analysis',
        'employee',
        'purpose',
        'is_approved',
        'signed_date',
        'created_at'
    )
    search_fields = (
        'appeal_letter__number',
        'price_analysis__number',
        'employee__full_name'
    )
    list_filter = ('purpose', 'is_approved', 'signed_date')
    autocomplete_fields = ('appeal_letter', 'price_analysis', 'employee')
    readonly_fields = ('created_at', 'updated_at')
