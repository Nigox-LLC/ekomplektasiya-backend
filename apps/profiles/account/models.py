from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from utils.models.base import BaseModel


class MyUsernameValidator(RegexValidator):
    regex = r'^[\w.@+\- ]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_/space characters.'
    )
    flags = 0


class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        # Using string directly to avoid circular dependency
        extra_fields.setdefault('role', 'admin')
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    class LanguageCode(models.TextChoices):
        UZ = 'uz', 'O\'zbek tili'
        RU = 'ru', 'Rus tili'
        EN = 'en', 'English'

    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        DISTRICT = 'district', 'Tuman'
        REGION = 'region', 'Viloyat'
        REPUBLIC = 'republic', 'Respublika'
        PURCHASER = 'purchaser', 'Komplektasiya'

    objects = CustomUserManager()

    username_validator = MyUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_/space only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    role = models.CharField(
        verbose_name='Foydalanuvchi turi',
        max_length=50,
        choices=Role.choices,
        default=Role.DISTRICT,
    )
    employee = models.ForeignKey(
        verbose_name='Foydalanuvchiga bog\'langan xodim',
        to='staff.Employee',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    language_code = models.CharField(
        verbose_name='Foydalanuvchi tilini tanlang',
        max_length=2,
        choices=LanguageCode.choices,
        default=LanguageCode.UZ,
    )

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['language_code']),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=['employee'],
                name='user_employee_unique'
            )
        ]

    def __str__(self) -> str:
        if hasattr(self, 'employee') and self.employee:
            return str(self.employee)
        return self.username

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username='{self.username}')>"

    def get_absolute_url(self) -> str:
        return reverse('user_detail', kwargs={'pk': self.pk})
