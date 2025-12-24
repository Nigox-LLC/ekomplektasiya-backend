from django.db import models
from utils.models.base import BaseModel
from apps.directory.area.models import Region, District



class Bank(BaseModel):
    mfo = models.CharField(max_length=50)
    stir = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20, blank=True, null=True)
    site_url = models.CharField(max_length=255,blank=True, null=True)
    geolocation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banklar'

        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['phone']),
            models.Index(fields=['name', 'stir']),
            models.Index(fields=['mfo', 'stir']),
            models.Index(fields=['region', 'district']),
        ]


class WareHouse(BaseModel):
    address = models.TextField(blank=True)
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Ombor'
        verbose_name_plural = 'Omborlar'

        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['phone']),
            models.Index(fields=['region', 'district']),
        ]

