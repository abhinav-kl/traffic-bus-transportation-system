# Generated by Django 4.2 on 2023-05-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficApp', '0008_rename_time_time_allocation_arrival_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='latitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bus',
            name='longitude',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
