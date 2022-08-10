from django.db import models
from Clientes.models import Cliente

# Create your models here.
class Marcastarjetas(models.Model):
    ttarjetas_id = models.AutoField(db_column='TTarjetas_id', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ttarjetas_marca = models.TextField(db_column='TTarjetas_Marca')  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'Tarjetas'