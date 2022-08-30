####################################################################
#
#   Contiene al paquete PrestamosPackage
#       Metodos:
#           - log_page: Se encarga de renderizar la pagina 
#               a partir de la informacion en la base de datos.
#               Utiliza informacion de Prestamos y Cliente.
#
#           - mensaje: Se encarga de renderizar una pagina
#               que contiene la respuesta frente a la solicitud
#               de prestamo. Ante falla en ingreso, aqui se estipula
#               de donde proviene el error.
#
#           Los ingresos son autenticados!
#
#   Contiene las clases PrestamoView, que permite la visualizacion
#       de los prestamos existentes segun corresponda con el 
#       usuario logeado.
#       - Read-Only Viewset
#       - Requiere autenticacion
#
#   Contiene la clase PrestamoEmpleado, que permite la creacion y 
#       eliminacion de solicitudes de prestamo. La accion, tanto
#       de cancelacion como aceptacion efectua modificaciones 
#       sobre el saldo de la cuenta.
#       - Requiere de Autenticacion para Staff
#       - Permite modificacion de datos
#   
#####################################################################

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Clientes.models import Cliente, Tipoclientes
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from Clientes.models  import *
from Cuentas.models   import *
from Tarjetas.models  import *
from Prestamos.models import *
from Api.serializers  import *

class PrestamoPackage:

    @login_required
    def log_page(request):
        
        user    = request.user
        prestamos = Prestamo.objects.filter(customer_id = user.id).order_by("-loan_date")
        cuenta = Cuenta.objects.filter(customer_id = user.id)
        content = {
            'prestamos':prestamos,
            'cuentas':cuenta
        }

        return render(request,"Prestamos/Prestamos.html",{'content':content})

    @login_required
    def mensaje(request):

        if request.method == 'POST':
            
            ################################
            # Parametros de Ingreso y de DB.
            user          = request.user
            
            cliente_tipo  = Cliente.objects.get(customer_id= user.id).id
            monto_maximo  = Tipoclientes.objects.get(tcliente_id = cliente_tipo).tcliente_limite_prestamo

            monto         = int(request.POST.get('Monto',0))
            tipo_prestamo = request.POST.get("seleccion_prestamo","")
            fecha         = request.POST.get("Fecha")
            cuenta        = request.POST.get("seleccion_cuenta","")

            ###############################
            # Checkeo parametros ingresados.
            opcion_prestamo = ["Hipotecario","Personal","Prendario"]
            opcion_prestamo_bool = tipo_prestamo in opcion_prestamo
            monto_zero_bool = monto > 0
            msg = ""

            if not opcion_prestamo_bool:
                msg = "Porfavor, seleccione el tipo de prestamo a tomar."
            
            elif not monto_zero_bool:
                msg = "Porfavor, ingrese un Monto a prestar mayor a cero."
            
            elif not cuenta.isnumeric():
                msg = "Ingrese el tipo de cuenta sobre la cual aplicar el prestamo."
            

            ################################
            # Checkeo segun tipo de cliente.
            if monto > monto_maximo:
                tcliente = Tipoclientes.objects.get(tcliente_id = cliente_tipo).tcliente_tipo
                msg = f"El monto solicitado supera al limite establecido para clientes {tcliente}."
                

            if msg == "":
                ###########################
                # Creacion de la solicitud.
                Prestamo.objects.create(
                    loan_type = tipo_prestamo,
                    loan_date = fecha,
                    loan_total = monto,
                    customer_id = user.id
                )

                ##################################
                # Update del balance de la cuenta.
                saldo_inicial = Cuenta.objects.get(account_id = int(cuenta)).balance
                Cuenta.objects.filter(account_id = cuenta).update(balance=saldo_inicial+monto)

                ######################################
                # Enviamos el mensaje correspondiente.
                msg = "Felicitaciones, su prestamo fue efectivamente consolidado."

            return render(request,'Prestamos/PrestamosStatus.html',{'msg':msg})   



class PrestamosView(viewsets.ReadOnlyModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):

        is_staff = self.request.user.is_staff
        ##############################
        # Configuracion para Clientes.
        if not is_staff:
            user = self.request.user
            data = Prestamo.objects.filter(customer_id = user.id)
            return data
        
        ################################
        # Confirguracion para Empleados.
        elif is_staff:
                        
            branch_id = self.request.GET.get("Sucursal","")

            if branch_id != "":

                clientes = Cliente.objects.filter(branch_id=branch_id)
                clientes_id = [x.customer_id for x in clientes]
                
                prestamos = Prestamo.objects.filter(customer_id__in =clientes_id)
                return prestamos
            
            else:
                return Prestamo.objects.all()


    def get_serializer_class(self):
        
        is_staff = self.request.user.is_staff

        if is_staff:
            return PrestamoSerializerEmpleado

        else:
            return PrestamoClienteSerializer



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

