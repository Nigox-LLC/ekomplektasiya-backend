from .models import PurchaseType
from utils.schema.exclude import BaseModelSerializer


class PurchaseTypeSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = PurchaseType