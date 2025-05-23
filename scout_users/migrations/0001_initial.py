# Generated by Django 4.2.20 on 2025-04-21 11:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import scout_users.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('country_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Phone Code')),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user_type', models.CharField(blank=True, choices=[('customer', 'Customer'), ('service_provider', 'Service Provider')], max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_description', models.TextField(blank=True, null=True)),
                ('user_rating', models.FloatField(blank=True, default=0.0, null=True)),
                ('user_rating_count', models.IntegerField(blank=True, default=0, null=True)),
                ('service_name', models.CharField(blank=True, max_length=50, null=True)),
                ('service_description', models.TextField(blank=True, null=True)),
                ('work_experience', models.IntegerField(blank=True, null=True)),
                ('availability_status', models.CharField(choices=[('available', 'Available'), ('busy', 'Busy'), ('unavailable', 'Unavailable')], default='available', max_length=50)),
                ('service_location', models.CharField(blank=True, max_length=100, null=True)),
                ('total_completed_jobs', models.IntegerField(blank=True, null=True)),
                ('required_documents', models.CharField(blank=True, max_length=255, null=True)),
                ('document_verification_status', models.BooleanField(default=False)),
                ('verification_status', models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('rejected', 'Rejected')], default='pending', max_length=50)),
                ('user_verified_documents', models.FileField(blank=True, null=True, upload_to=scout_users.models.ServiceProvider.service_provider_document_path)),
                ('portfolio_images', models.ImageField(blank=True, null=True, upload_to=scout_users.models.ServiceProvider.service_provider_portfolio_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_provider_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_language', models.CharField(blank=True, max_length=50, null=True)),
                ('subscription_plan', models.CharField(blank=True, max_length=50, null=True)),
                ('subscription_start_date', models.DateField(blank=True, null=True)),
                ('subscription_end_date', models.DateField(blank=True, null=True)),
                ('subscription_status', models.BooleanField(default=False)),
                ('profile_completion', models.IntegerField(default=0)),
                ('user_rating', models.FloatField(blank=True, default=0.0, null=True)),
                ('referral_code', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
