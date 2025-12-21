from typing import Tuple
from rest_framework.serializers import ModelSerializer, IntegerField


class BaseModelSerializer(ModelSerializer):
    id = IntegerField(read_only=True)
    class Meta:
        abstract = True
        exclude: Tuple[str, ...] = ('is_active', 'updated_at', 'created_at')