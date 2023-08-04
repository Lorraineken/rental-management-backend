from django.shortcuts import render
#from rest_framework import viewsets #for CRUD operations
from .serializers import PropertySerializer
from .models import Property

from rest_framework import generics

#class PropertyView(viewsets.ModelViewSet):
 #   serializer_class = PropertySerializer
 #   queryset = Property.objects.all()

class PropertyCreate(generics.CreateAPIView):
    #API endpoint that allows creation of a new property
    queryset = Property.objects.all(),
    serializer_class = PropertySerializer 

class PropertyList(generics.ListAPIView):
    # API endpoint that allows Properties to be viewed
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetail(generics.RetrieveAPIView):
    #API endpoint that returns a single property by pk
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyUpdate(generics.RetrieveUpdateAPIView):
    #API endpoint that allows updating of property record
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDelete(generics.RetrieveDestroyAPIView):
    #API endpoint that allows a property record to be deleted
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

