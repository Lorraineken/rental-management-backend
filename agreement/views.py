from django.shortcuts import render
#from rest_framework import viewsets
from .serializers import AgreementSerializer
from .models import Agreement

from rest_framework import generics

#The viewsets base class provides the implementation for CRUD operations
#  by default. This code specifies the serializer_class and the queryset.
# Create your views here.

#class AgreementView(viewsets.ModelViewSet):
#    serializer_class = AgreementSerializer
#    queryset = Agreement.objects.all()

class AgreementCreate(generics.CreateAPIView):
    #API endpoint that allows creation of a new Agreement
    queryset = Agreement.objects.all(),
    serializer_class = AgreementSerializer 

class AgreementList(generics.ListAPIView):
    # API endpoint that allows Agreements to be viewed
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

class AgreementDetail(generics.RetrieveAPIView):
    #API endpoint that returns a single agreement by pk
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

class AgreementUpdate(generics.RetrieveUpdateAPIView):
    #API endpoint that allows updating of agreement record
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

class AgreementDelete(generics.RetrieveDestroyAPIView):
    #API endpoint that allows an agreement record to be deleted
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

