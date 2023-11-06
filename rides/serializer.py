from rest_framework import serializers
from rides.models import Ride,Station

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'