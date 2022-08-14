from django.shortcuts import render,redirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Clientes.models import Cliente, Tipoclientes
from Prestamos.models import Prestamo

# Create your views here.

class PrestamoPackage:

    @login_required
    def log_page(request):
        
        user    = request.user
        prestamos = Prestamo.objects.filter(customer_id = user.id)
        return render(request,"Prestamos/Prestamos.html",{'prestamos':prestamos})

    @login_required
    def mensaje(request):

        if request.method == 'POST':

            user    = request.user
            
            cliente_tipo  = Cliente.objects.get(customer_id= user.id).id
            monto_maximo  = Tipoclientes.objects.get(tcliente_id = cliente_tipo).tcliente_limite_prestamo

            monto         = int(request.POST.get('Monto',0))
            tipo_prestamo = request.POST.get("seleccion_prestamo","")
            fecha = request.POST.get("Fecha")

            ###############################
            # Checkeo parametros ingresados.
            opcion_prestamo = ["Hipotecario","Personal","Prendario"]
            opcion_prestamo_bool = tipo_prestamo in opcion_prestamo
            monto_zero_bool = monto >= 0

            if not opcion_prestamo_bool:
                msg = "Porfavor, seleccione el tipo de prestamo a tomar."
            
            elif not monto_zero_bool:
                msg = "Porfavor, ingrese un Monto a prestar mayor a cero."
            

            ################################
            # Checkeo segun tipo de cliente.
            if monto > monto_maximo:
                tcliente = Tipoclientes.objects.get(tcliente_id = cliente_tipo).tcliente_tipo
                msg = f"El monto solicitado supera al limite establecido para clientes {tcliente}."
                return HttpResponse(msg)

            ###########################
            # Creacion de la solicitud.
            Prestamo.objects.create(
                loan_type = tipo_prestamo,
                loan_date = fecha,
                loan_total = monto,
                customer_id = user.id
            )

        return redirect(reverse('prestamos'))
