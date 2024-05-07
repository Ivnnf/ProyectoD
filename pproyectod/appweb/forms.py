import re
from django import forms
from .models import *
from django.contrib.auth.models import User, Group

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"

    def clean_telefono_contacto(self):
        telefono = self.cleaned_data.get('telefono_contacto')
        if telefono and len(telefono.replace(" ", "")) != 9:
            raise forms.ValidationError("El número de teléfono debe tener exactamente 9 dígitos.")
        return telefono
    def clean_correo_contacto(self):
        correo = self.cleaned_data.get('correo_contacto')
        if correo:
            # Expresión regular para validar un correo electrónico
            correo_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(correo_regex, correo):
                raise forms.ValidationError("Por favor, ingrese un correo electrónico válido.")
        return correo

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


