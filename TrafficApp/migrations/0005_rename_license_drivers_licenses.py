# Generated by Django 4.2 on 2023-05-03 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficApp', '0004_owners_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drivers',
            old_name='license',
            new_name='licenses',
        ),
    ]