from django.shortcuts import render
from rest_framework import viewsets #for CRUD operations
from .serializers import PaymentSerializer
from .models import Payment
# Create your views here.

class PaymentView(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
