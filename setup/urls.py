
from django.contrib import admin
from django.urls import include, path
from rides.views import StationViewSet,RidesViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('stations',StationViewSet,basename='Stations')
router.register('rides',RidesViewSet,basename='Rides')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
