from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from Clientes.models  import *
from Cuentas.models   import *
from Tarjetas.models  import *
from Prestamos.models import *
from Api.serializers  import *



class ClienteView(viewsets.ModelViewSet):
    
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        
        user = self.request.user
        data = Cliente.objects.filter(customer_id = user.id)
        return data



class CuentaView(viewsets.ModelViewSet):
    
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        user = self.request.user
        data = Cuenta.objects.filter(customer_id_id = user.id)
        return data



class PrestamosView(viewsets.ModelViewSet):

    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):

        usuario = "empleado"


        ####################
        # Configuracion para Clientes
        if usuario == "cliente":
            user = self.request.user
            data = Prestamo.objects.filter(customer_id = user.id)
            return data
        

        ################################
        # Confirguracion para Empleados.
        elif usuario == "empleado":
                        
            branch_id = self.request.GET.get("Sucursal","")

            if branch_id != "":

                clientes = Cliente.objects.filter(branch_id=branch_id)
                clientes_id = [x.customer_id for x in clientes]
                
                prestamos = Prestamo.objects.filter(customer_id__in =clientes_id)
                return prestamos
            
            else:
                return Prestamo.objects.all()
        


class TarjetasView(viewsets.ModelViewSet):

    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Tarjetas.objects.all()