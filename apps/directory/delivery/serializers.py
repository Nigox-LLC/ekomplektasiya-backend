from .models import DeliveryCondition
from utils.schema.exclude import BaseModelSerializer


class DeliveryConditionSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = DeliveryCondition
