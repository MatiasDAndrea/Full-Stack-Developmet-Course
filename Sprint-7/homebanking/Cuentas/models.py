from django.db import models
from Clientes.models import Cliente

# Create your models here.
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
    tcuenta_id = models.IntegerField(db_column='TCuenta_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cuenta'


class Movimientos(models.Model):
    cuenta_id = models.AutoField(db_column='Cuenta_id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    numcuenta = models.IntegerField(db_column='NumCuenta')  # Field name made lowercase.
    monto = models.IntegerField(db_column='Monto')  # Field name made lowercase.
    tipo_operacion = models.TextField(db_column='Tipo_Operacion')  # Field name made lowercase.
    hora = models.TextField(db_column='HORA')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Movimientos'