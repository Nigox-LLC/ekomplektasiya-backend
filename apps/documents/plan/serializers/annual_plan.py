import logging
from typing import Dict, Any
from django.utils import timezone
from rest_framework import serializers
from apps.documents.plan.models import AnnualPlan
from utils.schema.exclude import BaseModelSerializer
from apps.documents.plan.services.exceptions import AnnualPlanValidationError
from apps.documents.plan.services.annual_plan_service import AnnualPlanService
from .annual_plan_item import AnnualPlanItemCreateSerializer, AnnualPlanItemRetrieveSerializer


logger = logging.getLogger(__name__)


class AnnualPlanCreateSerializer(BaseModelSerializer):
    
    items = AnnualPlanItemCreateSerializer(many=True, min_length=1)
    

    class Meta(BaseModelSerializer.Meta):
        model = AnnualPlan
        
    def validate_for_year(self, value: int) -> int:
        current_year = timezone.now().year
        
        if value < current_year:
            raise serializers.ValidationError(
                f"O'tgan yillar uchun plan yaratib bo'lmaydi. Joriy yil: {current_year}"
            )
        
        if value > current_year + 5:
            raise serializers.ValidationError(
                f"5 yildan ko'proq kelasi yil uchun plan yaratish cheklangan. Joriy yil: {current_year}"
            )
        
        return value

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
       
        for_year = data.get('for_year')
        region = data.get('region')
        district = data.get('district')

        if AnnualPlan.objects.filter(
            for_year=for_year,
            region=region,
            district=district,
            is_active=True
        ).exists():
            raise serializers.ValidationError({
                'non_field_errors': _(
                    f"{for_year} yil uchun {region} - {district} "
                    "uchun aktiv plan allaqachon mavjud."
                )
            })
        
        return data

    def create(self, validated_data: Dict[str, Any]) -> AnnualPlan:
        try:
            return AnnualPlanService.save_annual_plan(validated_data)
        except AnnualPlanValidationError as e:
            raise serializers.ValidationError(e.detail)
        except Exception as e:
            logger.error(f"Plan yaratishda xatolik: {e}", exc_info=True)
            raise serializers.ValidationError({
                'non_field_errors': "Plan yaratishda xatolik yuz berdi. Iltimos qaytadan urinib ko'ring."
        })
    
    def update(self, instance: AnnualPlan, validated_data: Dict[str, Any]) -> AnnualPlan:

        validated_data['id'] = instance.id
        
        try:
            return AnnualPlanService.save_annual_plan(validated_data)
        except AnnualPlanValidationError as e:
            raise serializers.ValidationError(e.detail)
        except Exception as e:
            logger.error(f"Plan yangilashda xatolik: {e}", exc_info=True)
            raise serializers.ValidationError({
                'non_field_errors': "Plan yangilashda xatolik yuz berdi. Iltimos qaytadan urinib ko'ring."
            })
        

class AnnualPlanListSerializer(BaseModelSerializer):
    region_id = serializers.IntegerField(
        source='region.id',
        read_only=True, allow_null=True
    )
    region_name = serializers.CharField(
        source='region.name',
        read_only=True, allow_null=True
    )

    district_id = serializers.IntegerField(
        source='district.id',
        read_only=True, allow_null=True
    )
    district_name = serializers.CharField(
        source='district.name',
        read_only=True, allow_null=True
    )
    class Meta:
        model = AnnualPlan


class AnnualPlanRetrieveSerializer(BaseModelSerializer):
    items = AnnualPlanItemRetrieveSerializer(many=True, read_only=True)
    region_id = serializers.IntegerField(
        source='region.id',
        read_only=True, allow_null=True
    )
    region_name = serializers.CharField(
        source='region.name',
        read_only=True, allow_null=True
    )

    district_id = serializers.IntegerField(
        source='district.id',
        read_only=True, allow_null=True
    )
    district_name = serializers.CharField(
        source='district.name',
        read_only=True, allow_null=True
    )
    class Meta(BaseModelSerializer.Meta):
        model = AnnualPlan

