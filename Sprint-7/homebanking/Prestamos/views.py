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
#####################################################################

from django.shortcuts import render,redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Clientes.models import Cliente, Tipoclientes
from Cuentas.models import Cuenta
from Prestamos.models import Prestamo

class PrestamoPackage:

    @login_required
    def log_page(request):
        
        user    = request.user
        prestamos = Prestamo.objects.filter(customer_id = user.id)
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
