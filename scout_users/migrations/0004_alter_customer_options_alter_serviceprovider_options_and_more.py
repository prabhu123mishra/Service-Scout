# Generated by Django 4.2.20 on 2025-04-24 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scout_users', '0003_alter_user_address_alter_user_country_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer', 'verbose_name_plural': 'Customers'},
        ),
        migrations.AlterModelOptions(
            name='serviceprovider',
            options={'verbose_name': 'Service Provider', 'verbose_name_plural': 'Service Providers'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
