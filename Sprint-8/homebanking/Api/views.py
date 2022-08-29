from http.client import ResponseNotReady
from os import stat
from tabnanny import check
from urllib import response
from winreg import QueryInfoKey
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
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):

        customer_id = self.request.GET.get("Cliente","")

        if customer_id == "":
            return Tarjetas.objects.all()

        elif customer_id.isnumeric():
            return Tarjetas.objects.filter(customer=customer_id)



class PrestamoEmpleado(viewsets.ModelViewSet):

    serializer_class = PrestamoSerializerEmpleado
    permission_classes = [permissions.IsAdminUser]
    queryset = Prestamo.objects.all()

    @action(detail=False,methods=['POST'])
    def add_Prestamo(self,request):

        monto = request.data.get("loan_total","")
        tipo_prestamo = request.data.get("loan_type","")
        fecha = request.data.get("loan_date")
        id = request.data.get("customer_id","")
        cuenta = request.data.get("account_num")
        cuenta_num = Cuenta.objects.get(account_id = cuenta)
        customer = Cliente.objects.get(customer_id = id)

        saldo_inicial = Cuenta.objects.get(account_id = cuenta).balance
        Cuenta.objects.filter(account_id = cuenta).update(balance=saldo_inicial+monto)
        Prestamo.objects.create(
            loan_type = tipo_prestamo,
            loan_date = fecha,
            customer_id = customer,
            loan_total = monto,
            account_num = cuenta_num
        )
        return Response(request.data,status.HTTP_200_OK)


    def delete(self,request):

        monto         = request.data.get("loan_total","")
        tipo_prestamo = request.data.get("loan_type","")
        fecha         = request.data.get("loan_date")
        id            = request.data.get("customer_id","")
        cuenta        = request.data.get("account_num","")

        saldo_inicial = Cuenta.objects.get(account_id = cuenta).balance
        Cuenta.objects.filter(account_id = cuenta).update(balance = saldo_inicial - monto)
        Prestamo.objects.filter(
            loan_type   = tipo_prestamo,
            loan_date   = fecha,
            loan_total  = monto,
            customer_id = id,
            account_num = cuenta
        ).delete()
        return Response(request.data,status.HTTP_200_OK)



class DirectionsView(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        is_staff = self.request.user.is_staff   
        
        if is_staff:
            
            return DireccionClientes.objects.all()

        else :
            
            user = self.request.user.id
            return DireccionClientes.objects.filter(customer_id = user)

    
    def get_serializer_class(self):

        is_staff = self.request.user.is_staff   
        if is_staff:
            return DireccionSerializerEmpleado

        else :
            return DireccionSerializer

    
    def put(self,request):

        data = request.data
        is_staff = self.request.user.is_staff 
        
        calle     = data.get("calle","")
        numero    = data.get("numero","")
        ciudad    = data.get("ciudad","")
        provincia = data.get("provincia","")
        pais      = data.get("pais","")

        if is_staff:

            customer_id = data.get("customer_id","")
            check_items = [
                calle,
                numero,
                ciudad,
                provincia,
                pais,
                customer_id
            ]

            if "" not in check_items:

                DireccionClientes.objects.filter(
                    customer_id = customer_id
                ).update(
                    calle       = calle,
                    numero      = numero,
                    ciudad      = ciudad,
                    provincia   = provincia,
                    pais        = pais
                )
                return Response(request.data,status.HTTP_200_OK)
            
            else:
                return Response(request.data,status.HTTP_400_BAD_REQUEST)

        else:

            id = self.request.user.id
            check_items = [
                calle,
                numero,
                ciudad,
                provincia,
                pais,
                id
            ]
            
            if "" not in check_items:


                DireccionClientes.objects.filter(
                    customer_id = id
                ).update(
                    calle       = calle,
                    numero      = numero,
                    ciudad      = ciudad,
                    provincia   = provincia,
                    pais        = pais
                )  
                return Response(request.data,status.HTTP_200_OK)

            else:
                return Response(request.data,status.HTTP_400_BAD_REQUEST)

