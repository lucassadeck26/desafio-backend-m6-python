from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from cnab.serializers import CNABSerializer
from cnab.models import CNABS
# Create your views here.

class CNABView(APIView):
     serializer_class = CNABSerializer
    
   
     class Meta:
        model = CNABS
        fields = [
          "id_tipo_transacao",
          "data",
          "valor",
          "cpf",
          "cartao",
          "hora",
          "dono",
          "nomeLoja"
                ]
       

