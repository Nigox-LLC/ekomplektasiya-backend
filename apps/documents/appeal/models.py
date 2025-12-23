from django.db import models
from django.utils import timezone
from utils.models.base import BaseModel
from apps.documents.common.enum import PurposeType
from utils.common.path import appeal_letter_doc_upload_path, appeal_letter_pdf_upload_path


class AppealLetter(BaseModel):
    number = models.CharField(max_length=200)
    employee = models.ForeignKey(
        'staff.Employee',
        on_delete=models.PROTECT
    )
    file_doc = models.FileField(
        upload_to=appeal_letter_doc_upload_path, 
        null=True, blank=True
    )
    file_pdf = models.FileField(
        upload_to=appeal_letter_pdf_upload_path, 
        null=True, blank=True
    )
    is_approved = models.BooleanField(default=False)



class AppealLetterItem(BaseModel):
    appeal_letter = models.ForeignKey(
        AppealLetter, on_delete=models.PROTECT
    )
    price_analysis = models.ForeignKey(
        'analysis.PriceAnalysis', on_delete=models.PROTECT
    )



class AppealLetterSigned(BaseModel):
    appeal_letter = models.ForeignKey(
        AppealLetter, on_delete=models.PROTECT
    )
    price_analysis = models.ForeignKey(
        'analysis.PriceAnalysis', on_delete=models.PROTECT
    )
    employee = models.ForeignKey(
        'staff.Employee', on_delete=models.PROTECT
    )
    purpose = models.CharField(
        max_length=20,
        choices=PurposeType.choices,
    )
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    signed_date = models.DateTimeField(default=timezone.now)