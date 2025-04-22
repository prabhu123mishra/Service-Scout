from django.db import models
from scout_users.models import ServiceProvider
import uuid

class ScoutServices(models.Model):
    """
    Model representing a scout service.
    """
       
    class Meta:
        verbose_name = "Scout Service"
        verbose_name_plural = "Scout Services"  
    
    SERVICE_GENRES = (
        ('select', 'Select an option'),
        ('home_services', 'Home Services'),
        ('personal_care', 'Personal Care'),
        ('cleaning', 'Cleaning & Maintenance'),
        ('tech_support', 'Tech Support'),
        ('coaching_classes', 'Coaching & Classes'),
        ('vehicle_services', 'Vehicle Services'),
        ('home_improvement', 'Home Improvement'),
    )
    
    provider = models.ForeignKey(ServiceProvider, verbose_name="Service Provider", related_name="services",  on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255, blank=False)
    service_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    years_of_experience = models.IntegerField()
    service_description = models.TextField()
    service_genre = models.CharField(max_length=255, choices=SERVICE_GENRES, default='select', verbose_name='genre')
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='10% of total fees  will be deducted as platfrom fee')
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Discount %")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def service_image_path(instance, filename):
        return f'service_images/{instance.provider}/{filename}'
    
    service_images = models.ImageField(upload_to=service_image_path, blank=True,  null=True)
    
    def save(self, *args, **kwargs):
        if not self.service_uuid:
            service_part = uuid.uuid4()
            self.service_uuid = f"{self.provider.user.user_uuid}@{service_part}"
        super(ScoutServices, self).save(*args, **kwargs)
    
    
    @property
    def sale_price(self ):
        sale_value = "%.2f" % (float(self.fixed_price)*0.9)
        discounted_sale_value = sale_value*(self.discount/100)
        return discounted_sale_value

    def __str__(self):
        return self.service_name 
    
    
    