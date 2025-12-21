from utils.models.base import BaseModel
from django.db.models import CharField, Index, ForeignKey, PROTECT


class ProductType(BaseModel):
    name = CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Mahsulot turi'
        verbose_name_plural = 'Mahsulot turlari'

        indexes = [
            Index(fields=['name']),
        ]


class ProductModel(BaseModel):
    name = CharField(max_length=255, unique=True)
    product_type = ForeignKey(ProductType, on_delete=PROTECT)
    
    class Meta:
        verbose_name = 'Mahsulot modeli'
        verbose_name_plural = 'Mahsulot modellari'

        indexes = [
            Index(fields=['name']),
        ]