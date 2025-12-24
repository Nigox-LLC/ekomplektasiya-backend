from .models import Bank, WareHouse
from rest_framework import serializers
from utils.schema.exclude import BaseModelSerializer


class BankSerializer(BaseModelSerializer):
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
        model = Bank
        exclude = BaseModelSerializer.Meta.exclude + ('region', 'district',)
    

class WareHouseSerializer(BaseModelSerializer):
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
        model = WareHouse
        exclude = BaseModelSerializer.Meta.exclude + ('region', 'district',)
        
