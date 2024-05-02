# Generated by Django 5.0.3 on 2024-04-13 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0014_datos_alumnos_confirmar_password'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_Moderador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Moderador', models.CharField(max_length=50)),
                ('apellido_Moderador', models.CharField(max_length=50)),
                ('rut_Moderador', models.CharField(max_length=12)),
                ('telefono_Moderador', models.CharField(default='+569 ', max_length=20)),
                ('correo', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('confirmar_password', models.CharField(default='', max_length=20)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]
