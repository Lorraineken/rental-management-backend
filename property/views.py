from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import PropertySerializer
from .models import Property
# Create your views here.

class PropertyView(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
