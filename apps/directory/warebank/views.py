from typing import Type
from .models import Bank, WareHouse
from django.db.models import QuerySet
from utils.views.base import BaseModelViewSet
from .serializers import BankSerializer, WareHouseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class WareHouseViewSet(BaseModelViewSet):
    queryset: QuerySet[WareHouse] = WareHouse.objects.all()
    serializer_class: Type[WareHouseSerializer] = WareHouseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    filterset_fields = ['region', 'district']


class BankViewSet(BaseModelViewSet):
    queryset: QuerySet[Bank] = Bank.objects.all()
    serializer_class: Type[BankSerializer] = BankSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    filterset_fields = ['region', 'district']

