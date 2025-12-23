from django.urls import path, include
from .views import AnnualPlanViewSet
from rest_framework.routers import DefaultRouter

__all__ = ['urlpatterns']

router = DefaultRouter()

router.register('', AnnualPlanViewSet)


urlpatterns = [
    path('', include(router.urls)),
]