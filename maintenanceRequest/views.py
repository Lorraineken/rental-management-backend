from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import MaintenanceRequestSerializer
from .models import MaintenanceRequest
# Create your views here.

class MaintenanceRequestView(viewsets.ModelViewSet):
    serializer_class = MaintenanceRequestSerializer
    queryset = MaintenanceRequest.objects.all()
