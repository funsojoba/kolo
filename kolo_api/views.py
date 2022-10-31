from rest_framework import response
from rest_Framework.response import Response
from django.db import transaction
from .serializers import KoloSerializer, TransferSerializer

from .models import Kolo

# Create your views here.

from rest_framework.views import APIView


class WalletView(APIView):
    def get(self, request):
        kolo_qs = Kolo.objects.filter(owner=request.user).first()
        return Response(data=KoloSerializer(kolo_qs).data)
    
    def send_money(self, request, pk):
        kolo_qs = Kolo.objects.filter(owner=request.user).first()
        serializer = TransferSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        reciever = User.objects.filter(id=pk).first()
        
        amount_to_send = serializer.data.get("amount")
        
        if not reciever:
            return Response(errors={
                "user": "User does not exist"
            }, status= status.HTTP_400_BAD_REQUEST)
        
        if amount_to_send > kolo_qs.wallet_balance:
            return Response(errors={
                "amount": "Insurfficient balance"
            }, status= status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            reciever_wallet = Kolo.objects.filter(owner=reciever)
            reciever_wallet.wallet_balance += amount_to_send
            
            kolo_qs -= amount_to_send
            
            kolo_qs.save()
            reciever_wallet.save()
            
            
        
        
