from django.urls import path, include
from .views import DeliveryConditionViewSet
from rest_framework.routers import DefaultRouter

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('', DeliveryConditionViewSet, basename='region')

urlpatterns = [
    path('', include(router.urls)),
]