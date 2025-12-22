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


