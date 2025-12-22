from django.db import models
from django.utils import timezone
from utils.models.base import BaseModel
from utils.common.path import org_info_upload_path,stat_upload_path,tk_file_upload_path


class Commercial(BaseModel):
    number = models.CharField(
        max_length=255
    )
    date = models.DateTimeField(
        default=timezone.now
    )
    organization = models.CharField(
        max_length=300
    )
    stir = models.CharField(
        max_length=20
    )
    delivery_condition = models.ForeignKey(
        'delivery.DeliveryCondition', null=True, blank=True,
        on_delete=models.PROTECT
    )
    delivery_day = models.IntegerField()
    org_info = models.FileField(
        upload_to=org_info_upload_path,
        null=True, blank=True
    )
    stat = models.FileField(
        upload_to=stat_upload_path,
        null=True, blank=True
    )
    file = models.FileField(
        upload_to=tk_file_upload_path,
        null=True, blank=True
    )
    employee = models.ForeignKey(
        'staff.Employee', on_delete=models.PROTECT
    )