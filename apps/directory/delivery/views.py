from .models import DeliveryCondition
from utils.views.base import BaseModelViewSet
from .serializers import DeliveryConditionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class DeliveryConditionViewSet(BaseModelViewSet):
    queryset = DeliveryCondition.objects.all()
    serializer_class = DeliveryConditionSerializer
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]