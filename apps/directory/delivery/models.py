from django.db import models
from utils.models.base import BaseModel


class DeliveryCondition(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Yetkazib berish holati'
        verbose_name_plural = 'Yetkazib berish holatlari'