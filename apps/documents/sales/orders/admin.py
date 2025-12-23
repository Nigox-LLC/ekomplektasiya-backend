from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from unfold.decorators import display
from .models import (
    Order, OrderProduct, StatusOrder, PostedWebSite, 
    WordOrder, SignedWordOrder, Officer, Attachment
)


class OrderProductInline(TabularInline):
    model = OrderProduct
    extra = 0
    autocomplete_fields = [
        'annual_plan', 'product_type', 'product_model', 
        'size', 'unit', 'employee', 'posted_website'
    ]


class StatusOrderInline(TabularInline):
    model = StatusOrder
    extra = 0
    autocomplete_fields = ('employee',)


class OfficerInline(TabularInline):
    model = Officer
    extra = 0
    autocomplete_fields = ('employee',)


class AttachmentInline(TabularInline):
    model = Attachment
    extra = 0
    autocomplete_fields = ('employee', 'category')


class WordOrderInline(StackedInline):
    model = WordOrder
    extra = 0
    autocomplete_fields = ('employee', 'category')
    show_change_link = True


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = (
        'id',
        'incoming_number',
        'outgoing_number',
        'incoming_date',
        'communication_type_badge',
        'order_type_badge',
        'sender',
        'receiver',
        'is_approved_badge',
        'created_at'
    )
    search_fields = (
        'incoming_number', 'outgoing_number', 
        'sender__full_name', 'receiver__full_name',
        'region__name', 'district__name'
    )
    list_filter = (
        'communication_type', 'order_type', 
        'is_cancel', 'is_seen', 'is_approved',
        'incoming_date'
    )
    autocomplete_fields = ('main', 'region', 'district', 'sender', 'receiver')
    date_hierarchy = 'incoming_date'
    list_fullwidth = True
    list_filter_sheet = True
    inlines = [
        OrderProductInline, 
        StatusOrderInline, 
        OfficerInline, 
        AttachmentInline,
        WordOrderInline
    ]
    readonly_fields = ('created_at', 'updated_at')

    @display(
        description="Aloqa turi",
        ordering="communication_type",
        label={
            "Xat": "info",
            "Telefon": "warning", 
            "Email": "primary",
            "Portal": "success"
        },
    )
    def communication_type_badge(self, obj):
        return obj.communication_type

    @display(
        description="Buyurtma turi",
        ordering="order_type",
        label={
            "Ichki": "success",
            "Tashqi": "warning",
            "Tijorat": "primary",
        },
    )
    def order_type_badge(self, obj):
        return obj.order_type

    @display(
        description="Holati",
        ordering="is_approved",
        boolean=True,
    )
    def is_approved_badge(self, obj):
        return obj.is_approved


@admin.register(OrderProduct)
class OrderProductAdmin(ModelAdmin):
    list_display = ('id', 'order', 'product_type', 'quantity', 'created_at')
    search_fields = ('order__incoming_number', 'product_type__name')
    autocomplete_fields = ('order', 'product_type', 'product_model', 'size', 'unit', 'employee', 'posted_website')


@admin.register(WordOrder)
class WordOrderAdmin(ModelAdmin):
    list_display = ('id', 'order', 'employee', 'is_approved', 'created_at')
    search_fields = ('order__incoming_number',)
    autocomplete_fields = ('order', 'employee', 'category')


@admin.register(SignedWordOrder)
class SignedWordOrderAdmin(ModelAdmin):
    list_display = ('id', 'word_order', 'employee', 'created_at')
    autocomplete_fields = ('word_order', 'employee')


@admin.register(PostedWebSite)
class PostedWebSiteAdmin(ModelAdmin):
    list_display = ('id', 'employee', 'created_at')
    search_fields = ('employee__full_name',)
    autocomplete_fields = ('employee',)
