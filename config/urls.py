from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.db.models import Count, Q
from django.urls import path, include
from django.views.generic import TemplateView
# Import models inside the function to avoid circular imports during startup

def dashboard_callback(request, context):
    from django.apps import apps
    from django.db.models import Count, Sum
    from django.db.models.functions import TruncDay
    from django.utils import timezone
    from datetime import timedelta
    
    try:
        Order = apps.get_model('orders', 'Order')
        Employee = apps.get_model('staff', 'Employee')
        Commercial = apps.get_model('commercial', 'Commercial')
        PriceAnalysis = apps.get_model('analysis', 'PriceAnalysis')

        # Time ranges
        now = timezone.now()
        last_week = now - timedelta(days=7)

        # KPI 1: Total Orders (with chart)
        total_orders = Order.objects.count()
        orders_last_week = Order.objects.filter(created_at__gte=last_week).count()
        
        # Chart data: Orders per day for last 7 days
        orders_chart_data = (
            Order.objects.filter(created_at__gte=last_week)
            .annotate(day=TruncDay('created_at'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )
        # Format chart for Unfold: [[day_str, value], ...] or simple list of values if labels not needed
        # Unfold expects simple list of values for sparklines often, or specific format. 
        # Based on docs/examples: "chart": [[label, value], ...]
        chart_orders = [[entry['day'].strftime('%d'), entry['count']] for entry in orders_chart_data]

        # KPI 2: Commercial Offers (Revenue proxy)
        total_commercials = Commercial.objects.count()
        commercials_last_week = Commercial.objects.filter(created_at__gte=last_week).count()
        
        
        # KPI 3: Employees
        total_employees = Employee.objects.count()

        # KPI 4: Pending Actions
        pending_orders = Order.objects.filter(is_approved=False).count()

        context.update({
            "kpi": [
                {
                    "title": "Jami Buyurtmalar",
                    "metric": total_orders,
                    "metric_extra": f"+{orders_last_week} o'tgan haftada", 
                    "footer": "Oxirgi 7 kun",
                    "chart": chart_orders,
                    "color": "primary",
                },
                {
                    "title": "Tijorat Takliflari",
                    "metric": total_commercials,
                    "metric_extra": f"+{commercials_last_week} yangi",
                    "footer": "Faollik sathi",
                    "chart": [[1, 10], [2, 15], [3, 12], [4, 20]], # Dummy data for visual
                    "color": "success",
                },
                {
                    "title": "Tasdiqlash Kutilmoqda",
                    "metric": pending_orders,
                    "metric_extra": "Diqqat talab",
                    "footer": "Buyurtmalar",
                    "chart": [],
                    "color": "warning",
                },
                 {
                    "title": "Xodimlar",
                    "metric": total_employees,
                    "footer": "Jami shtat",
                    "chart": [],
                     "color": "info",
                },
            ],
        })
    except Exception as e:
        print(f"Dashboard Error: {e}")
        
    return context


urlpatterns = [
    path('', TemplateView.as_view(template_name='landing.html'), name='landing'),
    path('admin/', admin.site.urls),
    path('api/directory/', include('apps.directory.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
