from django.db import models
from django.utils import timezone
from utils.models.base import BaseModel
from apps.documents.sales.common.enum import (
    OrderType, CommunicationType, OrderProductType, PurposeType
)
from utils.common.path import (
    posted_upload_path, word_order_upload_path, signed_word_order_upload_path, 
    signed_pdf_order_upload_path, attachment_upload_path
)

class Order(BaseModel):
    main = models.ForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True
    )
    incoming_number = models.CharField(
        max_length=255, unique=True
    )
    outgoing_number = models.CharField(
        max_length=255, unique=True
    )
    incoming_date = models.DateTimeField(
        default=timezone.now
    )
    outgoing_date = models.DateTimeField(
        default=timezone.now
    )
    communication_type = models.CharField(
        choices=CommunicationType.choices, max_length=20
    )
    direction = models.CharField(
        max_length=255, null=True, blank=True
    )
    order_type = models.CharField(
        choices=OrderType.choices, max_length=20
    )
    region = models.ForeignKey(
        'area.Region',
        on_delete=models.PROTECT, related_name='orders',
    )
    
    district = models.ForeignKey(
        'area.District',
        on_delete=models.PROTECT, related_name='orders',
    )
    sender = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT, related_name='sender',
    )
    receiver = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT, related_name='receiver',
    )
    comment = models.TextField(blank=True)
    is_cancel = models.BooleanField(default=False)
    is_seen = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

        indexes = [
            models.Index(fields=['is_seen']),
            models.Index(fields=['is_cancel']),
            models.Index(fields=['order_type']),
            models.Index(fields=['is_approved']),
            models.Index(fields=['incoming_number']),
            models.Index(fields=['outgoing_number']),
            models.Index(fields=['sender', 'receiver']),
            models.Index(fields=['region', 'district']),
            models.Index(fields=['communication_type']),
            models.Index(fields=['incoming_date', 'outgoing_date']),
            models.Index(fields=['communication_type', 'order_type']),
            models.Index(fields=['outgoing_number', 'incoming_number']),
        ]


class StatusOrder(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    employee = models.ManyToManyField('staff.Employee')
    status = models.CharField(max_length=255)


class PostedWebSite(BaseModel):
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT,
    )
    file = models.FileField(
        upload_to=posted_upload_path, null=True, blank=True
    )


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    order_product_type = models.CharField(
        choices=OrderProductType.choices, max_length=50
    )
    annual_plan = models.ForeignKey(
        'plan.AnnualPlan', on_delete=models.PROTECT, 
        null=True, blank=True
    )
    product_name = models.CharField(
        max_length=500, null=True, blank=True
    )
    product_type = models.ForeignKey(
        'product.ProductType', on_delete=models.PROTECT, 
        null=True, blank=True
    )
    product_model = models.ForeignKey(
        'product.ProductModel', on_delete=models.PROTECT, 
        null=True, blank=True
    )
    size = models.ForeignKey(
        'measurement.Size', on_delete=models.PROTECT, 
        null=True, blank=True
    )
    unit = models.ForeignKey(
        'measurement.Unit', on_delete=models.PROTECT, 
        null=True, blank=True
    )
    quantity = models.FloatField()
    comment = models.TextField(blank=True)
    price_analysis_quantity = models.FloatField(default=0)
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT,
    )
    posted_website = models.ForeignKey(
        PostedWebSite, on_delete=models.PROTECT,
        null=True, blank=True
    )


class WordOrder(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT,
    )
    category = models.ForeignKey(
        'measurement.Category', on_delete=models.PROTECT, 
        null=True, blank=True
    )
    file = models.FileField(
        upload_to=word_order_upload_path, null=True, blank=True
    )
    is_approved = models.BooleanField(default=False)


class SignedWordOrder(BaseModel):
    word_order = models.ForeignKey(
        WordOrder, on_delete=models.PROTECT
    )
    file_doc = models.FileField(
        upload_to=signed_word_order_upload_path,
        null=True, blank=True
    )
    file_pdf = models.FileField(
        upload_to=signed_pdf_order_upload_path,
        null=True, blank=True,
    )
    qr_data = models.CharField(
        max_length=300, null=True, blank=True
    )
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT,
    )


class Officer(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT
    ) 
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT,
    )
    is_signed = models.BooleanField(default=False)
    signed_date = models.DateTimeField(null=True, blank=True)
    purpose = models.CharField(
        choices=PurposeType.choices, max_length=25
    )


class Attachment(BaseModel):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT
    ) 
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT,
    )
    category = models.ForeignKey(
        'measurement.Category', on_delete=models.PROTECT, 
        null=True, blank=True
    )
    file = models.FileField(
        upload_to=attachment_upload_path
    )
    