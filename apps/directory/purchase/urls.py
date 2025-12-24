from django.urls import path, include
from .views import PurchaseTypeViewSet
from rest_framework.routers import DefaultRouter

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('', PurchaseTypeViewSet, basename='model')


urlpatterns = [
    path('', include(router.urls)),
]