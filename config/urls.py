from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/directory/', include('apps.directory.urls')),
    path('api/document/', include('apps.documents.urls')),
]
