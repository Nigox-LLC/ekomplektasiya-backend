import os
import django
from django.urls import reverse
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

def check_url(name):
    try:
        url = reverse(name)
    except Exception as e:
        print(f"FAILURE: {name} -> {e}")

print("--- Checking Admin URLs (Failures Only) ---")
check_url("admin:orders_order_changelist")
check_url("admin:commercial_commercial_changelist")
check_url("admin:analysis_priceanalysis_changelist")
check_url("admin:plan_annualplan_changelist")
check_url("admin:appeal_appealletter_changelist")
check_url("admin:doc_purchase_purchasetypebank_changelist")
check_url("admin:purchase_purchasetype_changelist") # Directory purchase?
check_url("admin:product_productmodel_changelist")
check_url("admin:product_producttype_changelist")
check_url("admin:measurement_category_changelist")
check_url("admin:measurement_unit_changelist")
check_url("admin:area_region_changelist")
check_url("admin:organization_department_changelist")
check_url("admin:delivery_deliverycondition_changelist")
check_url("admin:profil_account_user_changelist")
check_url("admin:staff_employee_changelist")
check_url("admin:warebank_bank_changelist")
