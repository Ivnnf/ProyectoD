# Generated by Django 5.0.3 on 2024-05-05 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0025_alter_contacto_telefono_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_alumnos',
            name='carrera_Usuario',
            field=models.IntegerField(choices=[('Analista Programador Computacional', 'Analista Programador Computacional'), ('Contabilidad Tributaria', 'Contabilidad Tributaria'), ('Administración de Empresas', 'Administración de Empresas'), ('Desarrollo de Aplicaciones', 'Desarrollo de Aplicaciones'), ('ingeniería en Desarrollo de Software', 'ingeniería en Desarrollo de Software')], default=''),
        ),
    ]