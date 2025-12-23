from django.urls import path, include
from .views import UnitViewSet, SizeViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('unit/', UnitViewSet, basename='unit')
router.register('size/', SizeViewSet, basename='size')
router.register('category/', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]