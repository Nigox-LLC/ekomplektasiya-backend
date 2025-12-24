from rest_framework import serializers
from ..models import AnnualPlanItemMonth
from utils.schema.exclude import BaseModelSerializer
from django.core.validators import MinValueValidator, MaxValueValidator


class AnnualPlanItemMonthCreateSerializer(BaseModelSerializer):
    
    month = serializers.IntegerField(
        validators=[
            MinValueValidator(1, message="Oy raqami 1 dan kichik bo'lishi mumkun emas."),
            MaxValueValidator(12, message="Oy raqami 12 den katta bo'lishi mumkun emas."),
        ],
        help_text="Plan oy raqami (1-12)"
    )
    quantity = serializers.FloatField(
        validators=[MinValueValidator(0)]
    )

    price = serializers.FloatField(
        validators=[MinValueValidator(0)]
    )

    summa = serializers.FloatField(
        validators=[MinValueValidator(0)],
        help_text="Frontenddan keladi"
    )

    class Meta(BaseModelSerializer.Meta):
        model = AnnualPlanItemMonth
        fields = BaseModelSerializer.Meta.exclude + ('item',)


    def validate_month(self, value: int) -> int:
        if hasattr(self, 'parent') and hasattr(self.parent, 'initial_data'):
            months = [item.get('month') for item in self.parent.initial_data if item.get('month')]
            if months.count(value) > 1:
                raise serializers.ValidationError(
                    f"Oy {value} bir necha marta qo'shilgan. Har bir oy faqat bir martta bo'lishi kerak."
                )
        return value
    


class AnnualPlanItemMonthRetrieveSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = AnnualPlanItemMonth
        fields = BaseModelSerializer.Meta.exclude + ('item',)
       