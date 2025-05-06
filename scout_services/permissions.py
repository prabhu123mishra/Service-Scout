# permissions.py
from rest_framework import permissions

class IsServiceProvider(permissions.BasePermission):
    """
    Custom permission to only allow service providers to update or delete their services.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the logged-in user is the provider of the service
        return obj.provider.user == request.user
