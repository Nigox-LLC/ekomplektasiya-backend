from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.db.models import Count, Q
from django.urls import path, include
from django.views.generic import TemplateView
# Import models inside the function to avoid circular imports during startup




urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('admin/', admin.site.urls),
    path('api/directory/', include('apps.directory.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
