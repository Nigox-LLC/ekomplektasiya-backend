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


class OrderProductType(models.TextChoices):
    OUTSIDE_ANNUAL_PLAN = "outside_annual_plan", _("Yillik rejadan tashqari")
    ANNUAL_PLAN = "annual_plan", _("Yillik reja")
    SERVICE = "service", _("Xizmat")


class PurposeType(models.TextChoices):
    SIGNATORY = "signatory", _("Imzolovchi")
    APPROVER = "approver", _("Kelishuvchi")
    PERFORMER = "performer", _("Ijrochi")