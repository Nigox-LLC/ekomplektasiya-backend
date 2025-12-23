from django.db import models
from django.utils.translation import gettext_lazy as _


class AnnualPlanMonth(models.IntegerChoices):
        JANUARY = 1, _('Yanvar')
        FEBRUARY = 2, _('Fevral')
        MARCH = 3, _('Mart')
        APRIL = 4, _('Aprel')
        MAY = 5, _('May')
        JUNE = 6, _('Iyun')
        JULY = 7, _('Iyul')
        AUGUST = 8, _('Avgust')
        SEPTEMBER = 9, _('Sentabr')
        OCTOBER = 10, _('Oktabr')
        NOVEMBER = 11, _('Noyabr')
        DECEMBER = 12, _('Dekabr')



class PurposeType(models.TextChoices):
    SIGNING = "signing", _("Imzolash")
    APPROVAL = "approval", _("Kelishish")


class BankItemType(models.TextChoices):
      INCOME = "income", _("Kirim")
      EXPENSE = "expense", _("Chiqim")


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