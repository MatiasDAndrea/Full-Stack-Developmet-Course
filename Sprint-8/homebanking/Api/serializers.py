################################################
#
#   Modulo que contiene todos los serializer
#       utilizados para la creacion de la API.
#
################################################


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


class PrestamoClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = [
            'loan_type',
            'loan_total',
            'loan_date'
        ]


class PrestamoSerializerEmpleado(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = [
            'loan_type',
            'loan_date',
            'loan_total',
            'customer_id',
            'account_num'
        ]


class DireccionSerializerEmpleado(serializers.ModelSerializer):

    class Meta:
        model = DireccionClientes
        fields = [
            "calle",
            "numero",
            "ciudad",
            "provincia",
            "pais",
            "customer_id"
        ]


class DireccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DireccionClientes
        fields = [
            "calle",
            "numero",
            "ciudad",
            "provincia",
            "pais"
        ]


class DireccionSucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direccion
        fields = [
            "calle",
            "numero",
            "ciudad",
            "provincia",
            "pais"
        ]


class SucursalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sucursales
        fields = [
            'branch_id',
            'branch_number',
            'branch_name',
            'branch_address_id'
        ]

    def to_representation(self, instance):
        ev = super().to_representation(instance)
        
        for key,value in ev.items():
            
            if key == "branch_address_id":
                
                val = Sucursales.objects.get(branch_address_id = value).branch_address_id
                ev[key] = DireccionSucursalSerializer(val).data

        return ev
