# Generated by Django 5.1.4 on 2025-01-27 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_system', '0004_driver_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='username',
        ),
        migrations.AddField(
            model_name='driver',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ride_system.account'),
            preserve_default=False,
        ),
    ]
