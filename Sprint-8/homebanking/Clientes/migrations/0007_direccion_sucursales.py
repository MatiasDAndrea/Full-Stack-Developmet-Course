# Generated by Django 4.1 on 2022-08-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0006_cliente_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccion_id', models.AutoField(db_column='Direccion_id', primary_key=True, serialize=False)),
                ('calle', models.TextField(db_column='Calle')),
                ('numero', models.TextField(db_column='Numero')),
                ('ciudad', models.TextField(db_column='Ciudad')),
                ('provincia', models.TextField(db_column='Provincia')),
                ('pais', models.TextField(db_column='Pais')),
            ],
            options={
                'db_table': 'Direccion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursales',
                'managed': True,
            },
        ),
    ]