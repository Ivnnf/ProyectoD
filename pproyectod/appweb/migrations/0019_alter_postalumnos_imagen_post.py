# Generated by Django 5.0.3 on 2024-05-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0018_postalumnos_delete_postalumno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalumnos',
            name='imagen_post',
            field=models.ImageField(null=True, upload_to='AlumnosP'),
        ),
    ]