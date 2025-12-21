from typing import Type
from .models import Region, District
from django.db.models import QuerySet
from utils.views.base import BaseModelViewSet
from .serializers import RegionSerializer, DistrictSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class RegionViewSet(BaseModelViewSet):
    queryset: QuerySet[Region] = Region.objects.all()
    serializer_class: Type[RegionSerializer] = RegionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']


class DistrictViewSet(BaseModelViewSet):
    queryset: QuerySet[District] = District.objects.all().select_related('region')
    serializer_class:Type[DistrictSerializer] = DistrictSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['name']
    search_fields = ['name']
    filterset_fields = ['region']
    ordering_fields = ['id', 'name', 'region']