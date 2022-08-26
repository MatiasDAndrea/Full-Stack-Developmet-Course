from dataclasses import field
from imp import source_from_cache
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

        
class CuentaSerializer(serializers.ModelSerializer):
    
    tcuenta_id = serializers.ReadOnlyField(source = 'tcuenta_id.tcuenta_tipo')
    class Meta:
        model = Cuenta
        fields = [
            'account_id',
            'balance',
            'tcuenta_id'
        ]



class TarjetaSerializer(serializers.ModelSerializer):
    pass

class PrestamoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = [
            'loan_id',
            'loan_type',
            'loan_total'
        ]