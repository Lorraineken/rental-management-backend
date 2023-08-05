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
# views.py

class AgreementCreateView(generics.CreateAPIView):
    serializer_class = AgreementSerializer

    def perform_create(self, serializer):
        # Set the landlord_id based on the request data
        landlord_id = self.request.data.get('landlord_id')
        serializer.save(landlord_id=landlord_id)

# Agreement List View
class AgreementListView(generics.ListCreateAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

# Agreement Detail View
class AgreementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

# Agreement Create View
class AgreementCreateView(generics.CreateAPIView):
    serializer_class = AgreementSerializer

    def perform_create(self, serializer):
        # Set the landlord_id based on the request data
        landlord_id = self.request.data.get('landlord_id')
        serializer.save(landlord_id=landlord_id)

# Agreement Update View
class AgreementUpdateView(generics.UpdateAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

# Agreement Delete View
class AgreementDeleteView(generics.DestroyAPIView):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer

