from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Location
from .serializers import LocationSerializer

# Create your views here.

@api_view(['GET', 'DELETE', 'PUT']) # Methods Allowed

def get_delete_update_location(request, pk):  #pk es PrimaryKey(Id)
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        content = {
            'status': 'Not Found'
        }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    # details a sinlge movie
    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    # delete a movie
    elif request.method == 'DELETE':
        location.delete()
        content = {
            'status': 'NO CONTENT'
            }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
        
    # update a movie
    elif request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST']) 

def get_post_locations(request):
    # get all movies
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    # create a new movie
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)