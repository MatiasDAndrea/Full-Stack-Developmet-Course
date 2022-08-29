# Generated by Django 4.1 on 2022-08-29 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0008_alter_sucursales_branch_address_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionClientes',
            fields=[
                ('direccion_id', models.AutoField(db_column='Direccion_id', primary_key=True, serialize=False)),
                ('calle', models.TextField(db_column='Calle')),
                ('numero', models.TextField(db_column='Numero')),
                ('ciudad', models.TextField(db_column='Ciudad')),
                ('provincia', models.TextField(db_column='Provincia')),
                ('pais', models.TextField(db_column='Pais')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.IntegerField(default=1),
        ),
    ]
