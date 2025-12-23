from .models import Department, Position
from utils.schema.exclude import BaseModelSerializer


class PositionSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = Position


class DepartmentSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = Department