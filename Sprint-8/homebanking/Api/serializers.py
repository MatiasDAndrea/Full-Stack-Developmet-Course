from rest_framework import serializers
from Clientes.models  import *
from Cuentas.models   import *
from Tarjetas.models  import *
from Prestamos.models import *

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = [
            'customer_name',
            'customer_surname',
            'customer_dni',
            'dob',
            'branch_id'
        ]

    #def to_representation(self, instance):

        #dictionary_object = super().to_representation(instance)
        



class CuentaSerializer(serializers.ModelSerializer):
    pass

class TarjetaSerializer(serializers.ModelSerializer):
    pass

class PrestamoSerializer(serializers.ModelSerializer):
    pass

class CuentaSerializer(serializers.ModelSerializer):
    pass