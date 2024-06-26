# Generated by Django 5.0.6 on 2024-06-14 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_booking_product_remove_booking_quantity_and_more'),
        ('product', '0003_alter_cityservice_city_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingproduct',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.booking'),
        ),
        migrations.AlterField(
            model_name='bookingproduct',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_product', to='product.product'),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('time_slot', 'booking_time', 'assign_work')},
        ),
    ]
