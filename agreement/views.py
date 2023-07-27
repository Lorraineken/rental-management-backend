from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AgreementSerializer
from .models import Agreement

#The viewsets base class provides the implementation for CRUD operations
#  by default. This code specifies the serializer_class and the queryset.
# Create your views here.

class AgreementView(viewsets.ModelViewSet):
    serializer_class = AgreementSerializer
    queryset = Agreement.objects.all()
