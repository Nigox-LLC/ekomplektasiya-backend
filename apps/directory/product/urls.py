from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet, ProductTypeViewSet

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('model/', ProductModelViewSet, basename='model')
router.register('type/', ProductTypeViewSet, basename='type')


urlpatterns = [
    path('', include(router.urls)),
]