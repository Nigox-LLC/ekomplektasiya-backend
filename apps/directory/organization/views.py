from .models import Department, Position
from utils.views.base import BaseModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import DepartmentSerializer, PositionSerializer


class DepartmentViewSet(BaseModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]



class PositionViewSet(BaseModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    ordering = ['id']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]