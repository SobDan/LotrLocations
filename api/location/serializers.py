from .models import Location
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer): # create classs to serializer model    

    class Meta:
        model = Location
        fields = ('region', 'location', 'description', 'lon','lat','comments')