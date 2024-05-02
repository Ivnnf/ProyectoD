# Generated by Django 5.0.3 on 2024-05-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0017_postalumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostAlumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_post', models.CharField(max_length=50)),
                ('descripcion_post', models.TextField(max_length=200)),
                ('tipo_post', models.IntegerField(choices=[(1, 'Grupo Estudio'), (2, 'Grupo Equipo'), (3, 'Grupo Ocio')])),
                ('imagen_post', models.ImageField(null=True, upload_to='postAlum')),
            ],
        ),
        migrations.DeleteModel(
            name='PostAlumno',
        ),
    ]