from .models import Unit, Size, Category
from utils.views.base import BaseModelViewSet
from .serializers import UnitSerializer, SizeSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class UnitViewSet(BaseModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]



class SizeViewSet(BaseModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    ordering = ['id']
    search_fields = ['name']
    filterset_fields = ['product_model']
    ordering_fields = ['id', 'name', 'product_model']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


class CategoryViewSet(BaseModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]