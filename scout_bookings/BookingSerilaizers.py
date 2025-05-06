from rest_framework import serializers
from .models import ServiceBooking
from scout_users.models import Customer, ServiceProvider
from scout_services.models import ScoutServices


class ServiceBookingSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.user.username', read_only=True)
    provider_name = serializers.CharField(source='service_provider.user.username', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)
    progress = serializers.SerializerMethodField()

    class Meta:
        model = ServiceBooking
        fields = [
            'id',
            'customer',
            'customer_name',
            'provider_name',
            'service_name',
            'status',
            'booking_date',
            'booking_time',
            'created_at',
            'updated_at',
            'address',
            'special_instructions',
            'is_paid',
            'auto_cancel_time',
            'progress'
        ]
        read_only_fields = ['created_at', 'updated_at', 'progress']

    def get_progress(self, obj):
        return obj.progress()
