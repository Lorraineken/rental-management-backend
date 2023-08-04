from django.shortcuts import render
#from rest_framework import viewsets #for CRUD operations
from .serializers import UnitSerializer
from .models import Unit

from rest_framework import generics
# Create your views here.

#class UnitView(viewsets.ModelViewSet):
#    serializer_class = UnitSerializer
#    queryset = Unit.objects.all()

class UnitCreate(generics.CreateAPIView):
    #API endpoint that allows creation of a new unit
    queryset = Unit.objects.all(),
    serializer_class = UnitSerializer 

class UnitList(generics.ListAPIView):
    # API endpoint that allows Units to be viewed
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class UnitDetail(generics.RetrieveAPIView):
    #API endpoint that returns a single unit by pk
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class UnitUpdate(generics.RetrieveUpdateAPIView):
    #API endpoint that allows updating of unit record
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class UnitDelete(generics.RetrieveDestroyAPIView):
    #API endpoint that allows a unit record to be deleted
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
