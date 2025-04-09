from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "user_type",
                    "country_code",
                    "state",
                    "city",
                    "address",
                    "phone_number",
                    "is_verified",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + (
        "user_type",
        "is_verified",
        "state",
        "city",
    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "user_type",
        "is_verified",
        "is_active",
        "is_staff",
    )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Admin for Customer Users"""

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "preffered_language",
        "subscription_plan",
        "subscription_status",
        "profile_completion",
    )
    list_filter = (
        "subscription_plan",
        "subscription_status",
        "preffered_language",
    )
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "refferal_code",
    )


@admin.register(models.ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    """Admin for Service Providers"""

    list_display = (
        "username",
        "email",
        "service_name",
        "availability_status",
        "verification_status",
        "total_completed_jobs",
        "user_rating",
    )
    list_filter = (
        "availability_status",
        "verification_status",
        "service_location",
    )
    search_fields = (
        "username",
        "email",
        "service_name",
        "user_description",
    )
