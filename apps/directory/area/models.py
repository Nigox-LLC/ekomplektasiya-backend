from utils.models.base import BaseModel
from django.db.models import CharField, Index, ForeignKey, PROTECT, UniqueConstraint


class Region(BaseModel):
    name = CharField(max_length=255)
    prefix = CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'
        indexes = [
            Index(fields=['name']),
        ]


class District(BaseModel):
    name = CharField(max_length=255)
    region = ForeignKey(Region, on_delete=PROTECT)

    class Meta:
        verbose_name = 'Tauman'
        verbose_name_plural = 'Tumanlar'
        constraints = [
            UniqueConstraint(fields=['region', 'name'], name='area_unique_region_name')
        ]
        indexes = [
            Index(fields=['name']),
        ]