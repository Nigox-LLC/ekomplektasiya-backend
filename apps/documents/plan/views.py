from typing import Type
from .models import AnnualPlan
from django.db.models import QuerySet
from utils.views.base import BaseModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers.annual_plan import AnnualPlanCreateSerializer, AnnualPlanListSerializer, AnnualPlanRetrieveSerializer


class AnnualPlanViewSet(BaseModelViewSet):
    queryset: QuerySet[AnnualPlan] = AnnualPlan.objects.select_related('region', 'district').prefetch_related(
        'annualplanitem_set__annualplanitemmonth_set'
    ).all()
    serializer_class:Type[AnnualPlanListSerializer] = AnnualPlanListSerializer
    write_serializer_class: Type[AnnualPlanCreateSerializer] = AnnualPlanCreateSerializer
    retrieve_serializer_class: Type[AnnualPlanRetrieveSerializer] = AnnualPlanRetrieveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['region', 'district']

    