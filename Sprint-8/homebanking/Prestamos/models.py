from django.db import models
from Clientes.models import Cliente

# Create your models here.
class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente,on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'prestamo'