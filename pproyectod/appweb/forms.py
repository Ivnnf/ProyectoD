from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"


class AlumnosForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Datos_Alumnos
        fields = "__all__"       