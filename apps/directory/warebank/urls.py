from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BankViewSet, WareHouseViewSet

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('bank/', BankViewSet, basename='bank')
router.register('ware-house/', WareHouseViewSet, basename='type')


urlpatterns = [
    path('', include(router.urls)),
]