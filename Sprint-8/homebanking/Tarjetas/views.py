#########################################################
#
#   Clase : TarjetasView.
#       Permite a un empleado obtener la informacion
#           de todas las tarjetas de credito concedidas
#           a los clientes.
#
#########################################################

from rest_framework import viewsets
from rest_framework import permissions
from Clientes.models  import *
from Cuentas.models   import *
from Tarjetas.models  import *
from Prestamos.models import *
from Api.serializers  import *

class TarjetasView(viewsets.ReadOnlyModelViewSet):

    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):

        customer_id = self.request.GET.get("Cliente","")

        if customer_id == "":
            return Tarjetas.objects.all()

        elif customer_id.isnumeric():
            return Tarjetas.objects.filter(customer=customer_id)