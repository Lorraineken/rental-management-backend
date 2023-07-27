from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import LandlordSerializer
from .models import Landlord
# Create your views here.

class LandlordView(viewsets.ModelViewSet):
    serializer_class = LandlordSerializer
    queryset = Landlord.objects.all()
