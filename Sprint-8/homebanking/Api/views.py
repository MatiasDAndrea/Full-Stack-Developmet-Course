from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from Clientes.models  import *
from Cuentas.models   import *
from Tarjetas.models  import *
from Prestamos.models import *
from Api.serializers  import *

class ClienteView(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
