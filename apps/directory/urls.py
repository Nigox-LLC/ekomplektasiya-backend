from django.urls import path, include


urlpatterns = [
    path('area/', include('apps.directory.area.urls')),
    path('delivery/', include('apps.directory.delivery.urls')),
    path('measurement/', include('apps.directory.measurement.urls')),
    path('organization/', include('apps.directory.organization.urls')),
    path('product/', include('apps.directory.product.urls')),
]
