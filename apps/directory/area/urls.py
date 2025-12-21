from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegionViewSet, DistrictViewSet

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('regions', RegionViewSet, basename='region')
router.register('districts', DistrictViewSet, basename='district')


urlpatterns = [
    path('', include(router.urls)),
]