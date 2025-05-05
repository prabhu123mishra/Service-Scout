from rest_framework import serializers
from django.contrib.auth import get_user_model
# from scout_users.models import Customer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'username', 'password', 'email', 'first_name', 'last_name',
            'user_type', 'gender', 'profile_picture', 'country_code', 'state',
            'city', 'phone_number', 'address', 'is_verified', 'user_uuid',
        )

        read_only_fields = ('user_uuid', 'is_verified')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if instance.profile_picture and request:
            rep['profile_picture'] = request.build_absolute_uri(
                instance.profile_picture.url
                )
        return rep
