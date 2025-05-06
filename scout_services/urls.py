# urls.py
from django.urls import path
from .views import (
    ScoutServicesListView,
    ScoutServiceDetailView,
    ScoutServiceUpdateView,
    ScoutServiceDeleteView,
)

urlpatterns = [
    path('services/', ScoutServicesListView.as_view(), name='service-list'),  # List all services
    path('services/<int:pk>/', ScoutServiceDetailView.as_view(), name='service-detail'),  # Get service detail
    path('services/<int:pk>/update/', ScoutServiceUpdateView.as_view(), name='service-update'),  # Update service
    path('services/<int:pk>/delete/', ScoutServiceDeleteView.as_view(), name='service-delete'),  # Delete service
]
