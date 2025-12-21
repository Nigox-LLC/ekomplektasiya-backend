from .models import Region, District
from utils.schema.exclude import BaseModelSerializer
from rest_framework.serializers import CharField, IntegerField


class RegionSerializer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = Region


class DistrictSerializer(BaseModelSerializer):
    region_id = IntegerField(source='region.id', read_only=True)
    region_name = CharField(source='region.name', read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = District
        exclude = BaseModelSerializer.Meta.exclude + ('region',)