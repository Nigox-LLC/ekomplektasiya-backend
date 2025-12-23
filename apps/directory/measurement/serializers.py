from .models import Unit, Size, Category
from utils.schema.exclude import BaseModelSerializer
from rest_framework.serializers import IntegerField, CharField

class UnitSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = Unit


class CategorySerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = Category


class SizeSerializer(BaseModelSerializer):
    product_model_id = IntegerField(source='product_model.id', read_only=True)
    product_model_name = CharField(source='product_model.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = Size
        exclude = BaseModelSerializer.Meta.exclude + ('product_model',)


