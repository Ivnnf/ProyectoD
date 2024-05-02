from django import forms
from .models import *
from django.contrib.auth.models import User, Group

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"


class AlumnosForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Datos_Alumnos
        fields = "__all__"       
        widgets = {
            'password': forms.PasswordInput(),
            'confirmar_password': forms.PasswordInput(),
        }

class ModeradorForm(forms.ModelForm):
    class Meta:
        model = Datos_Moderador
        fields = "__all__"     
        widgets = {
            'password': forms.PasswordInput(),
            'confirmar_password': forms.PasswordInput(),
        }
    apellido_Moderador = forms.CharField(max_length=50)

class PublicacionForm (forms.ModelForm):
    class Meta: 
        model = PostAlumnos
        fields = ['nombre_post', 'descripcion_post', 'tipo_post', 'imagen_post']


