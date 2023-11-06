from rest_framework import viewsets,filters
from rides.models import  Ride,Station
from rides.serializer import RideSerializer,StationSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class RidesViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    filter_backends= [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_filter = ['id','user_gender','user_birthdate','user_residence','ride_date','time_start','time_end','station_start','station_end','ride_duration','ride_late']
    search_fields = ['id','user_gender','user_birthdate','user_residence','ride_date','time_start','time_end','station_start','station_end','ride_duration','ride_late']
    filterset_fields = ['ride_late']
class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_backends= [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_filter = ['id','station','station_number','station_name','lat','lon']
    ordering_filter = ['id','station','station_number','station_name','lat','lon']
    search_fields = ['id','station','station_number','station_name','lat','lon']
