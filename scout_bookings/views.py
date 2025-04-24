from rest_framework import generics, permissions
from .models import ServiceBooking
from scout_bookings.BookingSerilaizers import ServiceBookingSerializer
from scout_users.models import Customer, ServiceProvider
from rest_framework.exceptions import PermissionDenied, ValidationError
from django.shortcuts import get_object_or_404


class IsCustomerOrProvider(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.customer.user == request.user or
            obj.service_provider.user == request.user
        )


# 1. List bookings for a customer
class CustomerBookingListView(generics.ListAPIView):
    serializer_class = ServiceBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        customer = get_object_or_404(Customer, id=self.kwargs['customer_id'], user=self.request.user)
        return ServiceBooking.objects.filter(customer=customer)


# 2. List bookings for a provider
class ProviderBookingListView(generics.ListAPIView):
    serializer_class = ServiceBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        provider = get_object_or_404(ServiceProvider, id=self.kwargs['provider_id'], user=self.request.user)
        return ServiceBooking.objects.filter(service_provider=provider)


# 3. Detail view
class ServiceBookingDetailView(generics.RetrieveAPIView):
    queryset = ServiceBooking.objects.all()
    serializer_class = ServiceBookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomerOrProvider]


# 4. Delete booking
class ServiceBookingDeleteView(generics.DestroyAPIView):
    queryset = ServiceBooking.objects.all()
    serializer_class = ServiceBookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsCustomerOrProvider]


class CreateServiceBookingView(generics.CreateAPIView):
    queryset = ServiceBooking.objects.all()
    serializer_class = ServiceBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Get the logged-in customer
        try:
            customer = Customer.objects.get(user=self.request.user)
        except Customer.DoesNotExist:
            raise ValidationError("Only customers can book a service.")

        # Get the selected service from request
        service = serializer.validated_data.get('service')

        # Get the service provider associated with this service
        service_provider = service.service_provider  # Assuming your ScoutServices model has this FK

        # Save the booking
        serializer.save(customer=customer, service_provider=service_provider)