from django.db import models
from django.contrib.auth.models import User
# Create your models here.

tipos_contacto = [
    [0, "Consulta"],
    [1, "Sugerencia"],
    [2, "Problemas con tu cuenta"]

]

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=100)
    correo_contacto = models.CharField(max_length=100)
    telefono_contacto = models.IntegerField()
    mensaje_contacto = models.TextField()
    tipos_contacto = models.IntegerField(choices=tipos_contacto)
    def __srt__(self):
        return self.nombre_contacto + " "+self.correo_contacto
    



carreras = [

    [0, "Analista Programador Computacional"],
    [1, "Contabilidad Tributaria"],
    [2, "Administración de Empresas"],
    [3, "Desarrollo de Aplicaciones"],
    [4, "ingeniería en Desarrollo de Software"],
    

]

class Datos_Alumnos(models.Model):
    nombre_Usuario = models.CharField(max_length=50)
    apellido_Usuario = models.CharField(max_length=50)
    rut_Usuario = models.CharField(max_length=12)
    telefono_Usuario = models.CharField(max_length=20, default='+569 ')
    carrera_Usuario = models.IntegerField(choices=carreras, default='')
    semestre_Usuario = models.CharField(max_length=12,default='')
    correo = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre_Usuario