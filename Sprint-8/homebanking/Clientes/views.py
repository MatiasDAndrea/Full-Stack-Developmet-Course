#########################################################
#
#   Clases:
#       ClienteView : Se encarga de proveer la vista
#           de los datos de un cliente.
#           - Read-Only Model ViewSet.
#           - Necesita de Autenticacion.
#
#       DirectionView: Se encarga de gestionarle tanto al
#       usuario como al empleado la posibilidad de modificar
#       direcciones.
#       - Requiere de autenticacion.
#
#       Sucursales: Permite visualizar de forma global
#           todas las sucursales existentes.
#           - Read-Only.
#           - No requiere autenticacion.
#########################################################

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from Clientes.models  import *
from Api.serializers  import *

class ClienteView(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        user = self.request.user
        data = Cliente.objects.filter(customer_id = user.id)
        return data



class DirectionsView(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        is_staff = self.request.user.is_staff   
        
        if is_staff:
            
            return DireccionClientes.objects.all()

        else :
            
            user = self.request.user.id
            return DireccionClientes.objects.filter(customer_id = user)

    
    def get_serializer_class(self):

        is_staff = self.request.user.is_staff   
        if is_staff:
            return DireccionSerializerEmpleado

        else :
            return DireccionSerializer

    
    def put(self,request):

        data = request.data
        is_staff = self.request.user.is_staff 
        
        calle     = data.get("calle","")
        numero    = data.get("numero","")
        ciudad    = data.get("ciudad","")
        provincia = data.get("provincia","")
        pais      = data.get("pais","")

        if is_staff:

            customer_id = data.get("customer_id","")
            check_items = [
                calle,
                numero,
                ciudad,
                provincia,
                pais,
                customer_id
            ]

            if "" not in check_items:

                DireccionClientes.objects.filter(
                    customer_id = customer_id
                ).update(
                    calle       = calle,
                    numero      = numero,
                    ciudad      = ciudad,
                    provincia   = provincia,
                    pais        = pais
                )
                return Response(request.data,status.HTTP_200_OK)
            
            else:
                return Response(request.data,status.HTTP_400_BAD_REQUEST)

        else:

            id = self.request.user.id
            check_items = [
                calle,
                numero,
                ciudad,
                provincia,
                pais,
                id
            ]
            
            if "" not in check_items:


                DireccionClientes.objects.filter(
                    customer_id = id
                ).update(
                    calle       = calle,
                    numero      = numero,
                    ciudad      = ciudad,
                    provincia   = provincia,
                    pais        = pais
                )  
                return Response(request.data,status.HTTP_200_OK)

            else:
                return Response(request.data,status.HTTP_400_BAD_REQUEST)



class SucursalesView(viewsets.ReadOnlyModelViewSet):

    serializer_class = SucursalSerializer
    queryset = Sucursales.objects.all()