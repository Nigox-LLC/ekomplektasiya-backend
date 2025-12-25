from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role', 'employee', 'language_code')}),
        ('Metadata', {'fields': ('created_at', 'updated_at')}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'employee' in form.base_fields:
            form.base_fields['employee'].required = True
        return form

    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'is_staff', 'is_active', 'created_at'
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('created_at', 'updated_at', 'last_login', 'date_joined')
