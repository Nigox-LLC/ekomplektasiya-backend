from .models import Template
from rest_framework import serializers
from utils.schema.exclude import BaseModelSerializer


class TemplateSerializer(BaseModelSerializer):
    category_id = serializers.CharField(source="category.id", read_only=True, allow_null=True)
    category_name = serializers.CharField(source="category.name", read_only=True, allow_null=True)
    
    class Meta(BaseModelSerializer.Meta):
        model = Template
