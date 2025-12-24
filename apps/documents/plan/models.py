from django.db import models
from utils.models.base import BaseModel
from apps.documents.common.enum import AnnualPlanMonth


class AnnualPlan(BaseModel):
    for_year = models.IntegerField()
    region = models.ForeignKey(
        'area.Region', on_delete=models.PROTECT,related_name='anual_plan'
    )
    district = models.ForeignKey(
        'area.District', on_delete=models.PROTECT,related_name='anual_plan'
    )

    class Meta:
        verbose_name = "Yillik reja"
        verbose_name_plural = "Yillik rejalar"

        indexes = [
            models.Index(fields=['region', 'district']),
            models.Index(fields=['for_year'])
        ]


class AnnualPlanItem(BaseModel):
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(
        'measurement.Unit', on_delete=models.PROTECT,
        null=True, blank=True
    )
    is_approved = models.BooleanField(default=False)
    annual_plan = models.ForeignKey(AnnualPlan, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Yillik reja bandi'
        verbose_name_plural = 'Yillik reja bandlari'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['is_approved']),
            models.Index(fields=['annual_plan']),
        ]


class AnnualPlanItemMonth(BaseModel):
    item = models.ForeignKey(AnnualPlanItem, on_delete=models.PROTECT)
    month = models.PositiveSmallIntegerField(
        choices=AnnualPlanMonth.choices, verbose_name='Oy',
    )
    quantity = models.FloatField(verbose_name='Miqdori')
    price = models.FloatField(verbose_name='Narxi')
    summa = models.FloatField(verbose_name='Summasi')

    class Meta:
        verbose_name = 'Oylik reja '
        verbose_name_plural = 'Oylik rejalar'
        unique_together = ['item', 'month']
        ordering = ['month']
        indexes = [
            models.Index(fields=['item', 'month']),
        ]