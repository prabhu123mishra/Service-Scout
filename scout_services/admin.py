from django.contrib import admin
from .models import ScoutServices

@admin.register(ScoutServices)
class ScoutServicesAdmin(admin.ModelAdmin):
    list_display = (
        'service_name',
        'provider',
        'service_genre',
        'fixed_price',
        'discount',
        'created_at',
        'updated_at',
    )
    list_filter = ('service_genre', 'created_at', 'updated_at')
    search_fields = ('service_name', 'service_description', 'provider__user__email')
    readonly_fields = ('service_uuid', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': (
                'provider',
                'service_name',
                'service_genre',
                'service_description',
                'years_of_experience',
                'fixed_price',
                'discount',
                'service_images',
                'service_uuid',
                'created_at',
                'updated_at',
            )
        }),
    )
