# Generated by Django 4.1 on 2022-08-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tipoclientes',
            fields=[
                ('tcliente_id', models.AutoField(db_column='TCliente_id', primary_key=True, serialize=False)),
                ('tcliente_tipo', models.TextField(db_column='TCliente_tipo')),
                ('tcliente_descubrimiento', models.IntegerField(db_column='TCliente_descubrimiento')),
                ('tcliente_creditolim', models.IntegerField(db_column='TCliente_creditoLim')),
                ('tcliente_chequeralim', models.IntegerField(db_column='TCliente_chequeraLim')),
                ('tcliente_comision', models.IntegerField(db_column='TCliente_Comision')),
                ('tcliente_limite_transferencia', models.TextField(db_column='TCliente_Limite_Transferencia')),
                ('tcliente_crear_tarjeta', models.TextField(db_column='TCliente_Crear_Tarjeta')),
                ('tcliente_crear_chequera', models.TextField(db_column='TCliente_Crear_Chequera')),
                ('tcliente_comprar_dolar', models.TextField(db_column='TCliente_Comprar_Dolar')),
                ('tcliente_limite_extraccion', models.IntegerField(db_column='TCliente_Limite_Extraccion')),
            ],
            options={
                'db_table': 'TipoClientes',
                'managed': True,
            },
        ),
    ]
