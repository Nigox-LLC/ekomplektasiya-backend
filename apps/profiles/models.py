from django.contrib.auth.models import AbstractUser
from utils.models.base import BaseModel


class User(AbstractUser, BaseModel):
    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
