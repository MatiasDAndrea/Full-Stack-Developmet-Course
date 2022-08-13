from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


class CuentasPackage:

    @login_required
    def cuenta(request):
        #request.user
        return render(request,"Cuentas/cuenta.html")