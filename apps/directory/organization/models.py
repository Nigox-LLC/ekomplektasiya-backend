from utils.models.base import BaseModel
from django.db.models import CharField, Index


class Department(BaseModel):
    name = CharField(max_length=255, unique=True)
    index_number = CharField(max_length=200)

    class Meta:
        verbose_name = 'Bolim'
        verbose_name_plural = 'Bolimlar'

        indexes = [
            Index(fields=['name']),
        ]


class Position(BaseModel):
    name = CharField(max_length=255, unique=True)
     
    class Meta:
        verbose_name = 'Lavozim'
        verbose_name_plural = 'Lavozimlar'

        indexes = [
            Index(fields=['name']),
        ]