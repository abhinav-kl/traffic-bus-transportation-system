# Generated by Django 4.2 on 2023-04-23 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficApp', '0002_rename_login_id_traffic_police_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drivers',
            old_name='login_id',
            new_name='login',
        ),
        migrations.RenameField(
            model_name='owners',
            old_name='login_id',
            new_name='login',
        ),
        migrations.RenameField(
            model_name='passengers',
            old_name='login_id',
            new_name='login',
        ),
    ]
