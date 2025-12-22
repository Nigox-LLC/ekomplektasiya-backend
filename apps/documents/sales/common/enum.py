from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderType(models.TextChoices):
    INCOMING = "incoming", _("Kiruvchi")
    OUTGOING = "outgoing", _("Chiquvchi")


class CommunicationType(models.TextChoices):
    DISTRICT = "district", _("Tumandan")
    REGION = "region", _("Viloyatdan")
    REPUBLIC = "republic", _("Respublikadan")
    KOMPLEKTASIYA = "komplektasiya", _("Komplektasiyadan")
