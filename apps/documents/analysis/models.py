from django.db import models
from django.utils import timezone
from utils.models.base import BaseModel
from utils.common.path import price_analysis_upload_path


class PriceAnalysis(BaseModel):
    number = models.CharField(max_length=255)
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT, related_name='employees',
    )
    file = models.FileField(
        upload_to=price_analysis_upload_path
    )



class PriceAnalysisCommercial(BaseModel):
    price_analysis = models.ForeignKey(
        PriceAnalysis, on_delete=models.PROTECT
    )
    commercial = models.ForeignKey(
        'commercial.Commercial', on_delete=models.PROTECT
    )


class PriceAnalysisItem(BaseModel):
    price_analysis = models.ForeignKey(
        PriceAnalysis, on_delete=models.PROTECT
    )
    order_product = models.ForeignKey(
        'sales.orders.OrderProduct', on_delete=models.PROTECT
    )
    quantity = models.FloatField()
    price = models.FloatField()
    commercial_item = models.ManyToManyField(
        PriceAnalysisCommercial, blank=True
    )


class PriceAnalysisSigned(BaseModel):
    price_analysis = models.ForeignKey(
        PriceAnalysis, on_delete=models.PROTECT
    )
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT, related_name='employees',
    )
    is_approved = models.BooleanField(default=False)
    signed_date = models.DateTimeField(default=timezone.now)
