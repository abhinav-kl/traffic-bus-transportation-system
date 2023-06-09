# Generated by Django 4.2 on 2023-05-12 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficApp', '0012_remove_passengers_age_remove_passengers_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback_ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('bus_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus')),
                ('passenger_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.passengers')),
            ],
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='bus_id',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='passenger_id',
        ),
        migrations.DeleteModel(
            name='feedback',
        ),
        migrations.DeleteModel(
            name='ratings',
        ),
    ]
