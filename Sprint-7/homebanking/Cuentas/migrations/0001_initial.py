# Generated by Django 4.1 on 2022-08-13 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0002_cliente_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('cuenta_id', models.AutoField(db_column='Cuenta_id', primary_key=True, serialize=False)),
                ('numcuenta', models.IntegerField(db_column='NumCuenta')),
                ('monto', models.IntegerField(db_column='Monto')),
                ('tipo_operacion', models.TextField(db_column='Tipo_Operacion')),
                ('hora', models.TextField(db_column='HORA')),
            ],
            options={
                'db_table': 'Movimientos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipocuenta',
            fields=[
                ('tcuenta_id', models.AutoField(db_column='TCuenta_id', primary_key=True, serialize=False)),
                ('tcuenta_tipo', models.TextField(db_column='TCuenta_tipo')),
            ],
            options={
                'db_table': 'TipoCuenta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
                ('tcuenta_id', models.IntegerField(blank=True, db_column='TCuenta_id', null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.cliente')),
            ],
            options={
                'db_table': 'cuenta',
                'managed': True,
            },
        ),
    ]