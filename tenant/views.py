from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import TenantSerializer
from .models import Tenant

from rest_framework import generics
# Create your views here.

#class TenantView(viewsets.ModelViewSet):
 #   serializer_class = TenantSerializer
 #   queryset = Tenant.objects.all()

class TenantCreate(generics.CreateAPIView):
    #API endpoint that allows creation of a new tenant
    queryset = Tenant.objects.all(),
    serializer_class = TenantSerializer 

class TenantList(generics.ListAPIView):
    # API endpoint that allows Tenants to be viewed
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantDetail(generics.RetrieveAPIView):
    #API endpoint that returns a single tenant by pk
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantUpdate(generics.RetrieveUpdateAPIView):
    #API endpoint that allows updating of tenant record
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

class TenantDelete(generics.RetrieveDestroyAPIView):
    #API endpoint that allows a tenant record to be deleted
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
