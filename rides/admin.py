from django.contrib import admin
from rides.models import Station
from rides.models import Ride

class Stations(admin.ModelAdmin):
    list_display = ('id','station','station_number','station_name','lat','lon')
    list_display_links = ('id','station','station_number','station_name','lat','lon')
    search_fields = ('id','station','station_number','station_name','lat','lon')
    list_per_page = 10
admin.site.register(Station,Stations)

class Rides(admin.ModelAdmin):
    list_display = ('id','user_gender','user_birthdate','user_residence','ride_date','time_start','time_end','station_start','station_end','ride_duration','ride_late')
    list_display_links = ('id','user_gender','user_birthdate','user_residence','ride_date','time_start','time_end','station_start','station_end','ride_duration','ride_late')
    search_fields = ('id','user_gender','user_birthdate','user_residence','ride_date','time_start','time_end','station_start','station_end','ride_duration','ride_late')
    list_per_page = 10
admin.site.register(Ride,Rides)


