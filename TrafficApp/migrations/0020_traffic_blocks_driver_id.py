# Generated by Django 4.2 on 2023-05-15 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficApp', '0019_remove_traffic_blocks_bus_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic_blocks',
            name='driver_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.drivers'),
        ),
    ]
