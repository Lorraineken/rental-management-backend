from rest_framework import serializers
from .models import Agreement

class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields =('id','lease_terms','start_date','end_date')
