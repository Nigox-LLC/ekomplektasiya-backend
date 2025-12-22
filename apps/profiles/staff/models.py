from django.db import models
from django.urls import reverse
from utils.models.base import BaseModel
from .path import employee_image_upload_path
from django.core.validators import RegexValidator


class Employee(BaseModel):
    _phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Telefon: +998901234567 formatida bo'lishi kerak"
    )
    _inn_validator = RegexValidator(
        regex=r'^\d{14}$',
        message="INN 14 ta raqamdan iborat bo'lishi kerak"
    )
    _jshshr_validator = RegexValidator(
        regex=r'^\d{14}$',
        message="JSHSHIR 14 ta raqamdan iborat bo'lishi kerak"
    )
    _passport_series_validator = RegexValidator(
        regex=r'^[A-Z]{2}$',
        message="Passport seriyasi 2 ta bosh harf (AB, AC)"
    )
    _passport_number_validator = RegexValidator(
        regex=r'^\d{7}$',
        message="Passport raqami 7 ta raqamdan iborat"
    )
    
    full_name = models.CharField(
        max_length=400,
        verbose_name="F.I.O",
    )
    
    region = models.ForeignKey(
        'area.Region',
        on_delete=models.PROTECT, related_name='employees',
    )
    
    district = models.ForeignKey(
        'area.District',
        on_delete=models.PROTECT, related_name='employees',
    )
    
    department = models.ForeignKey(
        'organization.Department',
        on_delete=models.PROTECT, related_name='employees',
    )
    
    position = models.ForeignKey(
        'organization.Position',
        on_delete=models.PROTECT, related_name='employees',
    )
    
    inn = models.CharField(
        max_length=14, unique=True,null=True, blank=True,
        validators=[_inn_validator], verbose_name="INN"
    )
    
    phone = models.CharField(
        max_length=15,unique=True,null=True,blank=True,
        validators=[_phone_validator], verbose_name="Telefon",
    )
    
    address = models.TextField(
        blank=True, verbose_name="Manzil",
    )
    
    birth_date = models.DateField(
        null=True,blank=True,
        verbose_name="Tug'ilgan sana",
    )
    
    passport_series = models.CharField(
        max_length=2,null=True,blank=True,
        verbose_name="Passport seriyasi",
        validators=[_passport_series_validator],
    )
    
    passport_number = models.CharField(
        max_length=7,null=True,blank=True,
        validators=[_passport_number_validator],
        verbose_name="Passport raqami",
    )
    
    passport_image = models.ImageField(
        null=True,blank=True,
        upload_to=employee_image_upload_path,
        verbose_name="Passport nusxasi",
    )
    
    jshshr = models.CharField(
        max_length=14, unique=True, 
        null=True, verbose_name="JSHSHIR",
        blank=True, validators=[_jshshr_validator],
    )
    warehouse = models.ManyToManyField(
        'warebank.WareHouse', blank=True
    )
    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        
        indexes = [
            models.Index(fields=['full_name']),
            models.Index(fields=['inn', 'jshshr']),
            models.Index(fields=['region', 'district']),
            models.Index(fields=['department', 'position']),
        ]
        
        constraints = [
            models.UniqueConstraint(
                fields=['phone'],
                condition=models.Q(phone__isnull=False) & ~models.Q(phone=''),
                name='employee_phone_unique'
            ),
            models.UniqueConstraint(
                fields=['inn'],
                condition=models.Q(inn__isnull=False) & ~models.Q(inn=''),
                name='employee_inn_unique'
            ),
            models.UniqueConstraint(
                fields=['jshshr'],
                condition=models.Q(jshshr__isnull=False) & ~models.Q(jshshr=''),
                name='employee_jshshr_unique'
            ),
        ]
    
    def __str__(self) -> str:
        return self.full_name
    
    def __repr__(self) -> str:
        return f"<Employee(id={self.id}, name='{self.full_name}')>"
    
    def get_absolute_url(self) -> str:
        return reverse('employee_detail', kwargs={'pk': self.pk})
    

    