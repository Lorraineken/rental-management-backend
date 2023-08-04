from django.shortcuts import render
#from rest_framework import viewsets #for CRUD operations
from .serializers import LandlordSerializer
from .models import Landlord

from rest_framework import generics
# Create your views here.

#class LandlordView(viewsets.ModelViewSet):
#    serializer_class = LandlordSerializer
 #   queryset = Landlord.objects.all()

class LandlordCreate(generics.CreateAPIView):
    #API endpoint that allows creation of a new landlord
    queryset = Landlord.objects.all(),
    serializer_class = LandlordSerializer 

class LandlordList(generics.ListAPIView):
    # API endpoint that allows Landlords to be viewed
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class LandlordDetail(generics.RetrieveAPIView):
    #API endpoint that returns a single landlord by pk
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class LandlordUpdate(generics.RetrieveUpdateAPIView):
    #API endpoint that allows updating of landlord record
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer

class LandlordDelete(generics.RetrieveDestroyAPIView):
    #API endpoint that allows a landlord record to be deleted
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer