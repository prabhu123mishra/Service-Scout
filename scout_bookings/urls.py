from django.urls import path
from .views import (
    CustomerBookingListView,
    ProviderBookingListView,
    ServiceBookingDetailView,
    ServiceBookingDeleteView,
    CreateServiceBookingView,
)

urlpatterns = [
    path('users/<int:customer_id>/bookings/', CustomerBookingListView.as_view(), name='customer-bookings'),
    path('bookings/create/', CreateServiceBookingView.as_view(), name='booking-create'),
    path('providers/<int:provider_id>/bookings/', ProviderBookingListView.as_view(), name='provider-bookings'),
    path('bookings/<int:pk>/', ServiceBookingDetailView.as_view(), name='booking-detail'),
    path('bookings/<int:pk>/delete/', ServiceBookingDeleteView.as_view(), name='booking-delete'),
]
