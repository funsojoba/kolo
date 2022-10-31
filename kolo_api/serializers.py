from rest_framework import serializers
from .models import Kolo


class KoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kolo
        fields = '__all__'
        
        

class TransferSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=19, decimal_places=2)