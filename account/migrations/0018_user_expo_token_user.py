# Generated by Django 5.0.6 on 2024-07-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_subadminservicearea_city_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expo_token_user',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
