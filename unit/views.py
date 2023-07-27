from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import UnitSerializer
from .models import Unit
# Create your views here.

class UnitView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
