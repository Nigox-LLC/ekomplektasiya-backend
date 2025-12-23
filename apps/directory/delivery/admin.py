from django.contrib import admin
from .models import DeliveryCondition


@admin.register(DeliveryCondition)
class DeliveryConditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
