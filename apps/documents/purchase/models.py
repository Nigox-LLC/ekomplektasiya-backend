from django.db import models
from utils.models.base import BaseModel
from apps.documents.common.enum import BankItemType

class PurchaseTypeBank(BaseModel):
    purchase_type = models.ForeignKey(
        'product.ProductType', on_delete=models.PROTECT
    )
    number = models.CharField(max_length=255)
    bank = models.ForeignKey(
        'warebank.Bank', on_delete=models.PROTECT
    )
    balance = models.FloatField()



class PurchaseTypeBankItem(BaseModel):
    purchase_type_bank = models.ForeignKey(
        PurchaseTypeBank, on_delete=models.PROTECT
    )
    appeal_letter = models.ForeignKey(
        'appeal.AppealLetter', on_delete=models.PROTECT
    )
    bank_type = models.CharField(
        max_length=25,
        choices=BankItemType.choices
    )
    employee = models.ForeignKey(
        'staff.Employee', on_delete=models.PROTECT
    )
    summa = models.FloatField()


