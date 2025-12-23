from typing import Type
from .models import ProductType, ProductModel
from django.db.models import QuerySet
from utils.views.base import BaseModelViewSet
from .serializers import ProductTypeSerializer, ProductModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ProductTypeViewSet(BaseModelViewSet):
    queryset: QuerySet[ProductType] = ProductType.objects.all()
    serializer_class: Type[ProductTypeSerializer] = ProductTypeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']


class ProductModelViewSet(BaseModelViewSet):
    queryset: QuerySet[ProductModel] = ProductModel.objects.all().select_related('product_type')
    serializer_class:Type[ProductModelSerializer] = ProductModelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['name']
    search_fields = ['name']
    filterset_fields = ['product_type']
    ordering_fields = ['id', 'name', 'product_type']