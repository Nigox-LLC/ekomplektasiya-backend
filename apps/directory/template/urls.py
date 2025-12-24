from .views import TemplateViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('', TemplateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]