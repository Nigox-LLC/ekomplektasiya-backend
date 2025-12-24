from rest_framework import serializers
from utils.schema.exclude import BaseModelSerializer
from apps.documents.orders.models import Order



class OrderLsitSerialer(BaseModelSerializer):

    class Meta(BaseModelSerializer.Meta):
        model = Order