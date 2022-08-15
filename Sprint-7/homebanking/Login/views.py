############################################################
#
#   Contiene al paquete LoginPackage
#       Metodos:
#          - home: Realiza el render de la pagina de inicio.
#
############################################################

from django.shortcuts import render

class LoginPackage:

    def home(request):
        return render(request,"Login/home.html")


