# Generated by Django 5.0.6 on 2024-05-27 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_expo_token'),
        ('product', '0003_alter_cityservice_city_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('time_slot', 'booking_time', 'assign_work')},
        ),
    ]
