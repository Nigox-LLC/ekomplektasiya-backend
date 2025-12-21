from utils.base import BaseModel
from apps.directory.area.models import Region, District, PROTECT
from django.db.models import CharField, ForeignKey, Index, TextField


class Bank(BaseModel):
    mfo = CharField(max_length=50)
    stir = CharField(max_length=50)
    address = TextField(blank=True)
    city = CharField(max_length=100)
    short_name = CharField(max_length=100)
    name = CharField(max_length=255, unique=True)
    region = ForeignKey(Region, on_delete=PROTECT)
    district = ForeignKey(District, on_delete=PROTECT)
    phone = CharField(max_length=20, blank=True, null=True)
    site_url = CharField(max_length=255,blank=True, null=True)
    geolocation = CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banklar'

        indexes = [
            Index(fields=['name']),
            Index(fields=['phone']),
            Index(fields=['name', 'stir']),
            Index(fields=['mfo', 'stir']),
            Index(fields=['region', 'district']),
        ]


class WareHouse(BaseModel):
    address = TextField(blank=True)
    name = CharField(max_length=255, unique=True)
    region = ForeignKey(Region, on_delete=PROTECT)
    district = ForeignKey(District, on_delete=PROTECT)
    phone = CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = 'Ombor'
        verbose_name_plural = 'Omborlar'

        indexes = [
            Index(fields=['name']),
            Index(fields=['phone']),
            Index(fields=['region', 'district']),
        ]

