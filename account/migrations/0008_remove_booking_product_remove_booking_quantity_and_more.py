# Generated by Django 5.0.6 on 2024-06-07 08:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_booking_options_alter_booking_unique_together_and_more'),
        ('product', '0003_alter_cityservice_city_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='product',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='quantity',
        ),
        migrations.CreateModel(
            name='BookingProduct',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_product', to='account.booking')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]