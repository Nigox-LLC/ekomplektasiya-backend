from typing import Type
from .models import Template
from django.db.models import QuerySet
from .serializers import TemplateSerializer
from utils.views.base import BaseModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class TemplateViewSet(BaseModelViewSet):
    queryset: QuerySet[Template] = Template.objects.all()
    serializer_class: Type[TemplateSerializer] = TemplateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering = ['id']
    search_fields = ['name']
    filterset_fields = ['category']
    ordering_fields = ['id', 'name']


    def perform_create(self, serializer):
        employee = getattr(self.request.user, 'employee', None)
        serializer.save(employee=employee)