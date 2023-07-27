from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import CommunicationSerializer
from .models import Communication
# Create your views here.

class CommunicationView(viewsets.ModelViewSet):
    serializer_class = CommunicationSerializer
    queryset = Communication.objects.all()
