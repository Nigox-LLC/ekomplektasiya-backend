from utils.models.base import BaseModel
from apps.directory.product.models import ProductModel
from django.db.models import CharField, Index, TextField, ForeignKey, PROTECT


class Category(BaseModel):
    name = CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

        indexes = [
            Index(fields=['name']),
        ]


class Unit(BaseModel):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)

    class Meta:
        verbose_name = 'Birlik'
        verbose_name_plural = 'Birliklar'

        indexes = [
            Index(fields=['name']),
        ]


class Size(BaseModel):
    name = CharField(max_length=255, unique=True)
    product_model = ForeignKey(ProductModel, on_delete=PROTECT)

    class Meta:
        verbose_name = 'O‘lcham'
        verbose_name_plural = 'O‘lchamlar'

        indexes = [
            Index(fields=['name']),
        ]