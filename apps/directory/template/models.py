from django.db import models
from utils.models.base import BaseModel
from utils.common.path import template_upload_path


class Template(BaseModel):
    name = models.CharField(max_length=255)
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT, related_name='employees',
    )
    category = models.ForeignKey(
        'measurement.Category', on_delete=models.PROTECT, 
    )
    file = models.FileField(
        upload_to=template_upload_path,
    )