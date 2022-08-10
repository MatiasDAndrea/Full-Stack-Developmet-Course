from django.shortcuts import render

# Create your views here.

class CuentasPackage:
    def cuenta(request):
        return render(request,"Cuentas/cuenta.html")