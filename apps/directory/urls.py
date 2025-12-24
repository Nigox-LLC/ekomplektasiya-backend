from django.urls import path, include


urlpatterns = [
    path('area/', include('apps.directory.area.urls')),
    path('delivery/', include('apps.directory.delivery.urls')),
    path('measurement/', include('apps.directory.measurement.urls')),
    path('organization/', include('apps.directory.organization.urls')),
    path('product/', include('apps.directory.product.urls')),
    path('purchase/', include('apps.directory.purchase.urls')),
    path('template/', include('apps.directory.template.urls')),
    path('warebank/', include('apps.directory.warebank.urls')),
]
