from django.db import models

# Create your models here.

class Cliente(models.Model):

    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    id = models.IntegerField(db_column="TipoCliente")
    
    class Meta:
        managed = True
        db_table = 'cliente'


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


class Tipocuenta(models.Model):
    tcuenta_id = models.AutoField(db_column='TCuenta_id', primary_key=True)  # Field name made lowercase.
    tcuenta_tipo = models.TextField(db_column='TCuenta_tipo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TipoCuenta'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.TextField()
    tcuenta_id = models.ForeignKey(Tipocuenta,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'cuenta'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Marcastarjetas(models.Model):
    ttarjetas_id = models.AutoField(db_column='TTarjetas_id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ttarjetas_marca = models.TextField(db_column='TTarjetas_Marca')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'MarcasTarjetas'


class Tarjetas(models.Model):
    tarjetas_id = models.AutoField(db_column='Tarjetas_id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    tarjeta_numero = models.TextField(db_column='Tarjeta_Numero', unique=True)  # Field name made lowercase.
    tarjeta_cvv = models.TextField(db_column='Tarjeta_CVV')  # Field name made lowercase.
    tarjeta_fecha_otorgamiento = models.TextField(db_column='Tarjeta_Fecha_Otorgamiento')  # Field name made lowercase.
    tarjeta_fecha_expiracion = models.TextField(db_column='Tarjeta_Fecha_Expiracion')  # Field name made lowercase.
    tarjeta_tipo = models.TextField(db_column='Tarjeta_tipo')  # Field name made lowercase.
    ttarjetas = models.ForeignKey(Marcastarjetas, models.DO_NOTHING, db_column='TTarjetas_id')  # Field name made lowercase.
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    asignacion = models.TextField(db_column='Asignacion')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tarjetas'


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