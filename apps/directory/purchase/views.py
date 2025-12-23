from typing import Type
from .models import PurchaseType
from django.db.models import QuerySet
from utils.views.base import BaseModelViewSet
from .serializers import PurchaseTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class PurchaseTypeViewSet(BaseModelViewSet):
    queryset: QuerySet[PurchaseType] = PurchaseType.objects.all()
    serializer_class: Type[PurchaseTypeSerializer] = PurchaseTypeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']

