# views.py
from rest_framework import serializers, permissions
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from scout_services.models import ScoutServices
from scout_services.ServiceSerializers import ScoutServicesSerializer
from scout_services.permissions import IsServiceProvider

# 1. **List all services** - Accessible to both logged-in and unlogged users
class ScoutServicesListView(ListCreateAPIView):
    queryset = ScoutServices.objects.all()
    serializer_class = ScoutServicesSerializer
    permission_classes = [permissions.AllowAny]  

# 2. **Service details view** - Accessible to both logged-in and unlogged users
class ScoutServiceDetailView(RetrieveAPIView):
    queryset = ScoutServices.objects.all()
    serializer_class = ScoutServicesSerializer
    permission_classes = [permissions.AllowAny]  

# 3. **Update service** - Accessible only to the service provider who created it
class ScoutServiceUpdateView(UpdateAPIView):
    queryset = ScoutServices.objects.all()
    serializer_class = ScoutServicesSerializer
    permission_classes = [IsServiceProvider]  

    def get_queryset(self):
        service = super().get_queryset()
        return service.filter(provider=self.request.user.service_provider_profile)

# 4. **Delete service** - Accessible only to the service provider who created it
class ScoutServiceDeleteView(DestroyAPIView):
    queryset = ScoutServices.objects.all()
    permission_classes = [IsServiceProvider]  

    def get_queryset(self):
        service = super().get_queryset()
        return service.filter(provider=self.request.user.service_provider_profile)

