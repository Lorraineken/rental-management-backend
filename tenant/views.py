from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import TenantSerializer
from .models import Tenant
# Create your views here.

class TenantView(viewsets.ModelViewSet):
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()
