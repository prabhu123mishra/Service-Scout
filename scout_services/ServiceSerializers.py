from rest_framework import serializers
from .models import ScoutServices


class ScoutServicesSerializer(serializers.ModelSerializer):
    provider_uuid = serializers.UUIDField(source="provider.user_uuid", read_only=True)
    provider_name = serializers.CharField(
        source="provider.user.get_full_name", read_only=True
    )

    class Meta:
        model = ScoutServices
        fields = [
            "id",
            "provider",
            "provider_uuid",
            "provider_name",
            "service_name",
            "service_genre",
            "service_description",
            "years_of_experience",
            "fixed_price",
            "discount",
            "service_images",
            "service_uuid",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["service_uuid", "created_at", "updated_at", "sale_price"]
