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