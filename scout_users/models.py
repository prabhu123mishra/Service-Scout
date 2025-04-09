from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    """Parent class for all users in the system."""
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USER_TYPE = (
        ('customer', 'Customer'),
        ('service_provider', 'Service Provider'),
    )
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    user_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='other', null=True, blank=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE, default='customer')  # Removed 'None'
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    country_code = models.CharField(max_length=10, null=True, blank=True, verbose_name='Phone Code')
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(User):
    """Customer class for all user customers in the system."""

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'   

    preffered_language = models.CharField(max_length=50, null=True, blank=True)
    subscription_plan = models.CharField(max_length=50, null=True, blank=True)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)
    subscription_status = models.BooleanField(default=False)
    profile_completion = models.IntegerField(default=0)
    refferal_code = models.CharField(max_length=50, null=True, blank=True)


class ServiceProvider(User):

    class Meta:
        verbose_name = 'Service Provider'
        verbose_name_plural = 'Service Providers'

    AVAILABILITY = (
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('unavailable', 'Unavailable'),
    )
    VERIFICATION_STATUS = (
        ('pending', 'Pending'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
    )

    user_description = models.TextField(null=True, blank=True)
    user_rating = models.FloatField(null=True, blank=True)
    user_rating_count = models.IntegerField(null=True, blank=True)
    service_name = models.CharField(max_length=50, null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    work_experience = models.IntegerField(null=True, blank=True)
    availability_status = models.CharField(max_length=50, choices=AVAILABILITY, default='available')
    service_location = models.CharField(max_length=100, null=True, blank=True)
    total_completed_jobs = models.IntegerField(null=True, blank=True)
    required_documents = models.CharField(max_length=255, null=True, blank=True)
    document_verification_status = models.BooleanField(default=False)

    def service_provider_document_path(instance, filename):
        return f'documents/{instance.user_uuid}/{filename}'

    def service_provider_portfolio_path(instance, filename):
        return f'portfolio/{instance.user_uuid}/{filename}'

    user_verified_documents = models.FileField(upload_to=service_provider_document_path, null=True, blank=True)
    verification_status = models.CharField(max_length=50, choices=VERIFICATION_STATUS, default='pending')
    portfolio_images = models.ImageField(upload_to=service_provider_portfolio_path, null=True, blank=True)
