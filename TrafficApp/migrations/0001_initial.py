# Generated by Django 4.2 on 2023-04-23 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=100)),
                ('registration_number', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='bus_routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='bus_stops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop', models.CharField(max_length=100)),
                ('route_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus_routes')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('usertype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('login_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='traffic_police',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
                ('control_room', models.CharField(max_length=100)),
                ('login_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='traffic_blocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('stop_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus_stops')),
            ],
        ),
        migrations.CreateModel(
            name='time_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
                ('bus_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus')),
                ('stop_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus_stops')),
            ],
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=100)),
                ('bus_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus')),
                ('passenger_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.passengers')),
            ],
        ),
        migrations.CreateModel(
            name='owners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('place', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('association_ID', models.CharField(max_length=100)),
                ('login_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('passenger_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.passengers')),
            ],
        ),
        migrations.CreateModel(
            name='drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('license', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('login_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.login')),
            ],
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=500)),
                ('complaint_date', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=500)),
                ('reply_date', models.CharField(max_length=100)),
                ('passenger_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.passengers')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='owner_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.owners'),
        ),
        migrations.AddField(
            model_name='bus',
            name='route_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TrafficApp.bus_routes'),
        ),
    ]
