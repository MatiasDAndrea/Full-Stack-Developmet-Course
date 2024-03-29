# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Direcciones(models.Model):
    direccion_id = models.AutoField(db_column='Direccion_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    calle = models.TextField(db_column='Calle')  # Field name made lowercase.
    numero = models.TextField(db_column='Numero')  # Field name made lowercase.
    ciudad = models.TextField(db_column='Ciudad')  # Field name made lowercase.
    provincia = models.TextField(db_column='Provincia')  # Field name made lowercase.
    pais = models.TextField(db_column='Pais')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Direcciones'


class Marcastarjetas(models.Model):
    ttarjetas_id = models.AutoField(db_column='TTarjetas_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    ttarjetas_marca = models.TextField(db_column='TTarjetas_Marca')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MarcasTarjetas'


class Movimientos(models.Model):
    cuenta_id = models.AutoField(db_column='Cuenta_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    numcuenta = models.IntegerField(db_column='NumCuenta')  # Field name made lowercase.
    monto = models.IntegerField(db_column='Monto')  # Field name made lowercase.
    tipo_operacion = models.TextField(db_column='Tipo_Operacion')  # Field name made lowercase.
    hora = models.TextField(db_column='HORA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movimientos'


class Tarjetas(models.Model):
    tarjetas_id = models.AutoField(db_column='Tarjetas_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    tarjeta_numero = models.TextField(db_column='Tarjeta_Numero', unique=True)  # Field name made lowercase.
    tarjeta_cvv = models.TextField(db_column='Tarjeta_CVV')  # Field name made lowercase.
    tarjeta_fecha_otorgamiento = models.TextField(db_column='Tarjeta_Fecha_Otorgamiento')  # Field name made lowercase.
    tarjeta_fecha_expiracion = models.TextField(db_column='Tarjeta_Fecha_Expiracion')  # Field name made lowercase.
    tarjeta_tipo = models.TextField(db_column='Tarjeta_tipo')  # Field name made lowercase.
    ttarjetas = models.ForeignKey(Marcastarjetas, models.DO_NOTHING, db_column='TTarjetas_id')  # Field name made lowercase.
    customer = models.ForeignKey('Cliente', models.DO_NOTHING)
    asignacion = models.TextField(db_column='Asignacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tarjetas'


class Tipocliente(models.Model):
    tcliente_id = models.AutoField(db_column='TCliente_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'TipoCliente'


class Tipocuenta(models.Model):
    tcuenta_id = models.AutoField(db_column='TCuenta_id', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    tcuenta_tipo = models.TextField(db_column='TCuenta_tipo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoCuenta'


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField()
    new_id = models.IntegerField()
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.TextField()
    new_iban = models.TextField()
    old_type = models.IntegerField()
    new_type = models.IntegerField()
    user_action = models.TextField()
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tcuenta_id = models.IntegerField(db_column='TCuenta_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuenta'


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'
