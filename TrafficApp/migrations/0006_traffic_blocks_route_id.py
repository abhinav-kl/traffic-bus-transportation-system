# Generated by Django 4.2 on 2023-05-03 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficApp', '0005_rename_license_drivers_licenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic_blocks',
            name='route_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus_routes'),
        ),
    ]