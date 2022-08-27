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
    
    ttarjetas = serializers.ReadOnlyField(source = 'ttarjetas.ttarjetas_marca')
    class Meta:
        model = Tarjetas
        fields = [
            'tarjeta_numero',
            'tarjeta_cvv',
            'tarjeta_fecha_otorgamiento',
            'tarjeta_fecha_expiracion',
            'tarjeta_tipo',
            'tarjeta_tipo',
            'ttarjetas'
        ]


class PrestamoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = [
            'loan_id',
            'loan_type',
            'loan_total'
        ]