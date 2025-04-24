from django.db import models
from django.utils import timezone
from datetime import datetime
from scout_users.models import Customer, ServiceProvider
from scout_services.models import ScoutServices


class ServiceBooking(models.Model):
    # Status Constants
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    service_name = models.ForeignKey(ScoutServices, on_delete=models.CASCADE, related_name='booked_services')
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Optional extras
    address = models.TextField(help_text="Service address or location details")
    special_instructions = models.TextField(blank=True, null=True, help_text="Any extra notes from the customer")
    is_paid = models.BooleanField(default=False)
    
    # Auto-cancellation
    auto_cancel_time = models.DateTimeField(blank=True, null=True, help_text="Optional: cancel if not confirmed by this time")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Service Booking'
        verbose_name_plural = 'Service Bookings'

    def __str__(self):
        return f"{self.customer} booked {self.service_name} with {self.service_name.provider} on {self.booking_date} at {self.booking_time}"

    def is_upcoming(self):
        """Check if the booking is in the future."""
        booking_datetime = timezone.make_aware(datetime.combine(self.booking_date, self.booking_time))
        return booking_datetime > timezone.now()

    def auto_cancel_if_needed(self):
        """Auto-cancel the booking if it's not confirmed by a deadline."""
        if self.status == self.STATUS_PENDING and self.auto_cancel_time and timezone.now() > self.auto_cancel_time:
            self.status = self.STATUS_CANCELLED
            self.save()

    def progress(self):
        """Return progress percentage and label for UI purposes."""
        progress_map = {
            self.STATUS_PENDING: {"label": "Pending", "progress": 10},
            self.STATUS_CONFIRMED: {"label": "Confirmed", "progress": 40},
            self.STATUS_IN_PROGRESS: {"label": "In Progress", "progress": 70},
            self.STATUS_COMPLETED: {"label": "Completed", "progress": 100},
            self.STATUS_CANCELLED: {"label": "Cancelled", "progress": 0},
        }
        return progress_map.get(self.status, {"label": "Unknown", "progress": 0})
