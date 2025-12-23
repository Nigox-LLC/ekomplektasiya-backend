from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, PositionViewSet

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('department/', DepartmentViewSet, basename='department')
router.register('position', PositionViewSet, basename='position')

urlpatterns = [
    path('', include(router.urls)),
]