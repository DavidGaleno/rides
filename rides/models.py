from django.db import models

class Station(models.Model):
    station = models.CharField(max_length=255)
    station_number = models.IntegerField(unique=True)
    station_name = models.CharField(max_length=255)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    def __str__(self):
        return self.station_name
from django.db import models

class Ride(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    BOOLEAN_CHOICES = (
        (0, 'False'),
        (1, 'True'),
    )

    user_gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    user_birthdate = models.DateField(null=True, blank=True)
    user_residence = models.CharField(max_length=255,null=True, blank=True)
    ride_date = models.DateField(null=True, blank=True)
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    station_start = models.ForeignKey(Station,on_delete=models.PROTECT,related_name='ride_start')
    station_end = models.ForeignKey(Station,on_delete=models.PROTECT,related_name='ride_end')
    ride_duration = models.FloatField(null=True, blank=True)
    ride_late = models.BooleanField(null=True, blank=True,choices=BOOLEAN_CHOICES)


