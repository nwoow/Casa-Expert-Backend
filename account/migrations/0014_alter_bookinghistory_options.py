# Generated by Django 5.0.6 on 2024-06-28 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_booking_options_bookinghistory_assignby_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinghistory',
            options={'ordering': ['-created_at']},
        ),
    ]