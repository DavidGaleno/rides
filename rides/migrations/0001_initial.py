# Generated by Django 4.2.7 on 2023-11-06 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=255)),
                ('station_number', models.IntegerField()),
                ('station_name', models.CharField(max_length=255)),
                ('lat', models.CharField(max_length=20)),
                ('lon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user_birthdate', models.DateField(blank=True, null=True)),
                ('user_residence', models.CharField(blank=True, max_length=255, null=True)),
                ('ride_date', models.DateField(blank=True, null=True)),
                ('time_start', models.TimeField(blank=True, null=True)),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('ride_duration', models.FloatField(blank=True, null=True)),
                ('ride_late', models.BooleanField(blank=True, choices=[(0, 'False'), (1, 'True')], null=True)),
                ('station_end', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ride_end', to='rides.station')),
                ('station_start', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ride_start', to='rides.station')),
            ],
        ),
    ]
