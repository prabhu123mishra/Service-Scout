from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Customer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'user_type',
            'gender', 'profile_picture', 'country_code', 'state', 'city',
            'phone_number', 'address', 'is_verified', 'user_uuid',
        )
        read_only_fields = ('user_uuid', 'is_verified')