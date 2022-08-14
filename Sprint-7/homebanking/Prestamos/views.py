from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

class PrestamoPackage:
    

    def log_page(request):
        
        return render(request,"Prestamos/Prestamos.html")

    def mensaje(request):

        if request.method == 'POST':
            monto         = request.POST.get('Monto',0)
            tipo_prestamo = request.POST.get("tipoprestamo","").lower()

            ###############################
            # Checkeo parametros ingresados.
            opcion_prestamo = ["hipotecario","personal","prendario"]
            monto_bool = monto > 0
            tipo_prestamo_bool = tipo_prestamo in opcion_prestamo
            
            ################################
            # Checkeo segun tipo de cliente.




        return redirect(reverse('prestamos'))
