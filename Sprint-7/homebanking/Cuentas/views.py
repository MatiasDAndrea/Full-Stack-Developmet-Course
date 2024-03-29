#############################################################################
#   
#   Contiene al paquete CuentasPackage
#       Metodos del paquete:
#            - cuenta: Se encarga de tomar la informacion de la base de datos
#               y realizar el correspondiente render sobre la pagina cuentas.
#
#            - gocripto_render: Realiza el render de la pagina goCripto.
#
#############################################################################


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Clientes.models import Cliente
from Cuentas.models import Cuenta,Movimientos
from Tarjetas.models import Tarjetas,Marcastarjetas
from django.contrib.auth.models import User


class CuentasPackage:

    @login_required
    def cuenta(request):
        
        #############################################
        # Se obtiene el objeto del usuario ingresado.
        user    = request.user
        cliente = Cliente.objects.get(customer_id = user.id)
    
        ####################
        # Nombre de usuario.
        nombre = f"{cliente.customer_name} {cliente.customer_surname}"
        
        ##################
        # Datos de cuenta.
        cuenta = Cuenta.objects.filter(customer_id = user.id)
        
        #################
        # Datos Tarjetas.
        tarjetas = Tarjetas.objects.filter(customer_id = user.id)

        ####################
        # Datos Movimientos.
        movimientos = Movimientos.objects.filter(numcuenta = user.id)

        content = {
            "nombre": nombre,
            "cuentas":cuenta,
            "tarjetas":tarjetas,
            "movimientos":movimientos
        }
        return render(request,"Cuentas/cuenta.html",{'content':content})

    @login_required
    def gocripto_render(request):
        return render(request,"Cuentas/goCripto.html")