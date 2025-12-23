from .models import ProductModel, ProductType
from utils.schema.exclude import BaseModelSerializer
from rest_framework.serializers import CharField, IntegerField


class ProductTypeSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = ProductType


class ProductModelSerializer(BaseModelSerializer):
    product_type_id = IntegerField(source='product_type.id', read_only=True, allow_null=True)
    product_type_name = CharField(source='product_type.name', read_only=True, allow_null=True)

    class Meta(BaseModelSerializer.Meta):
        model = ProductModel
        exclude = BaseModelSerializer.Meta.exclude + ('product_type',)



