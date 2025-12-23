from django.apps import apps
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import timedelta

def dashboard_callback(request, context):
    print("DASHBOARD CALLBACK EXECUTING") # Verification log
    try:
        with open('debug_dashboard.txt', 'a') as f:
            f.write(f"Callback executed at {timezone.now()}\n")
    except Exception as e:
        print(f"File write error: {e}")

    # Initialize metrics with default 0
    total_orders = 0
    orders_last_week = 0
    total_commercials = 0
    commercials_last_week = 0
    total_employees = 0
    pending_orders = 0
    chart_orders = []

    try:
        Order = apps.get_model('orders', 'Order')
        Employee = apps.get_model('staff', 'Employee')
        Commercial = apps.get_model('commercial', 'Commercial')
        
        # Time ranges
        now = timezone.now()
        last_week = now - timedelta(days=7)

        # KPI 1: Total Orders
        total_orders = Order.objects.count()
        orders_last_week = Order.objects.filter(created_at__gte=last_week).count()
        
        # Chart data
        orders_chart_data = (
            Order.objects.filter(created_at__gte=last_week)
            .annotate(day=TruncDay('created_at'))
            .values('day')
            .annotate(count=Count('id'))
            .order_by('day')
        )
        chart_orders = [[entry['day'].strftime('%d'), entry['count']] for entry in orders_chart_data]

        # KPI 2: Commercial Offers
        total_commercials = Commercial.objects.count()
        commercials_last_week = Commercial.objects.filter(created_at__gte=last_week).count()
        
        # KPI 3: Employees
        total_employees = Employee.objects.count()

        # KPI 4: Pending Actions
        pending_orders = Order.objects.filter(is_approved=False).count()

    except Exception as e:
        print(f"Dashboard Data Error: {e}")
        # Consider logging this error properly

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
                "chart": [[1, 10], [2, 15], [3, 12], [4, 20]], 
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
            {
                "title": "TEST KPI",
                "metric": "100",
                "footer": "Static Data",
                "chart": [[1, 5], [2, 10]],
                "color": "error",
            },
        ],
    })
        
    return context
