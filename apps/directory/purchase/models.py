from django.db import models
from utils.models.base import BaseModel


class PurchaseType(BaseModel):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'Xarid turi'
        verbose_name_plural = 'Xarid turlari'

        indexes = [
            models.Index(fields=['name'])
        ]
