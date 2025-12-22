from django.db import models
from django.utils import timezone
from utils.models.base import BaseModel
from apps.documents.sales.common.enum import OrderType, CommunicationType


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

        index = [
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


