
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

 

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empleado'



class Tipoclientes(models.Model):
    tcliente_id = models.AutoField(db_column='TCliente_id', primary_key=True)  # Field name made lowercase.
    tcliente_tipo = models.TextField(db_column='TCliente_tipo')  # Field name made lowercase.
    tcliente_descubrimiento = models.IntegerField(db_column='TCliente_descubrimiento')  # Field name made lowercase.
    tcliente_creditolim = models.IntegerField(db_column='TCliente_creditoLim')  # Field name made lowercase.
    tcliente_chequeralim = models.IntegerField(db_column='TCliente_chequeraLim')  # Field name made lowercase.
    tcliente_comision = models.IntegerField(db_column='TCliente_Comision')  # Field name made lowercase.
    tcliente_limite_transferencia = models.TextField(db_column='TCliente_Limite_Transferencia')  # Field name made lowercase.
    tcliente_crear_tarjeta = models.TextField(db_column='TCliente_Crear_Tarjeta')  # Field name made lowercase.
    tcliente_crear_chequera = models.TextField(db_column='TCliente_Crear_Chequera')  # Field name made lowercase.
    tcliente_comprar_dolar = models.TextField(db_column='TCliente_Comprar_Dolar')  # Field name made lowercase.
    tcliente_limite_extraccion = models.IntegerField(db_column='TCliente_Limite_Extraccion')  # Field name made lowercase.
    tcliente_limite_prestamo  = models.IntegerField(db_column='TCliente_Prestamo')

    class Meta:
        managed = True
        db_table = 'TipoClientes'

    
class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sucursal'


class Direcciones(models.Model):
    direccion_id = models.AutoField(db_column='Direccion_id', primary_key=True)  # Field name made lowercase.
    calle = models.TextField(db_column='Calle')  # Field name made lowercase.
    numero = models.TextField(db_column='Numero')  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad')  # Field name made lowercase.
    provincia = models.TextField(db_column='Provincia')  # Field name made lowercase.
    pais = models.TextField(db_column='Pais')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Direcciones'


class DireccionClientes(models.Model):
    direccion_id = models.AutoField(db_column='Direccion_id', primary_key=True)  # Field name made lowercase.
    calle = models.TextField(db_column='Calle')  # Field name made lowercase.
    numero = models.TextField(db_column='Numero')  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad')  # Field name made lowercase.
    provincia = models.TextField(db_column='Provincia')  # Field name made lowercase.
    pais = models.TextField(db_column='Pais')  # Field name made lowercase.
    customer_id = models.IntegerField(default=1)


class Direccion(models.Model):
    direccion_id = models.AutoField(db_column='Direccion_id', primary_key=True)  # Field name made lowercase.
    calle = models.TextField(db_column='Calle')  # Field name made lowercase.
    numero = models.TextField(db_column='Numero')  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad')  # Field name made lowercase.
    provincia = models.TextField(db_column='Provincia')  # Field name made lowercase.
    pais = models.TextField(db_column='Pais')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Direccion'


class Sucursales(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.ForeignKey(Direccion,on_delete=models.CASCADE,default=1)

    class Meta:
        managed = True
        db_table = 'sucursales'


class Cliente(models.Model):

    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    id = models.IntegerField(db_column="TipoCliente")
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,default=1)
    direccion = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'cliente'