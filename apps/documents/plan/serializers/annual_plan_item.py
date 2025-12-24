from ..models import AnnualPlanItem
from rest_framework import serializers
from utils.schema.exclude import BaseModelSerializer
from django.utils.translation import gettext_lazy as _
from .annual_plan_item_month import AnnualPlanItemMonthCreateSerializer, AnnualPlanItemMonthRetrieveSerializer


class AnnualPlanItemCreateSerializer(BaseModelSerializer):
    
    months = AnnualPlanItemMonthCreateSerializer(many=True, min_length=1)
    is_approved = serializers.BooleanField(
        read_only=True,
        help_text="Avtomatik ravishda False bo'ladi"
    )

    class Meta(BaseModelSerializer.Meta):
        model = AnnualPlanItem
        exclude = BaseModelSerializer.Meta.exclude + ('annual_plan', )

    def validate_months(self, value: list) -> list:
        if not value:
            raise serializers.ValidationError(
                _("Plan uchun kamida bitta oy ma'lumotlari bo'lishi kerak.")
            )
        
        value.sort(key=lambda x: x['month'])
        return value

    def validate_name(self, value: str) -> str:
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                _("Element nomi kamida 3 belgidan iborat bo'lishi kerak.")
            )
        return value.strip().capitalize()
    



class AnnualPlanItemRetrieveSerializer(BaseModelSerializer):
    
    months = AnnualPlanItemMonthRetrieveSerializer(many=True, read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = AnnualPlanItem
        exclude = BaseModelSerializer.Meta.exclude + ('annual_plan', )