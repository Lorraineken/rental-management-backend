from django.shortcuts import render
# from rest_framework import viewsets #for CRUD operations
# from .serializers import MaintenanceRequestSerializer
# from .models import MaintenanceRequest
# # Create your views here.

# class MaintenanceRequestView(viewsets.ModelViewSet):
#     serializer_class = MaintenanceRequestSerializer
#     queryset = MaintenanceRequest.objects.all()
from rest_framework import generics
from .models import MaintenanceRequest
from .serializers import MaintenanceRequestSerializer

class MaintenanceRequestCreate(generics.CreateAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class MaintenanceRequestList(generics.ListAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class MaintenanceRequestDetail(generics.RetrieveAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class MaintenanceRequestUpdate(generics.RetrieveUpdateAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

class MaintenanceRequestDelete(generics.RetrieveDestroyAPIView):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
