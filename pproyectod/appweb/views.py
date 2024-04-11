from django.shortcuts import render,redirect,get_list_or_404
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q


# Create your views here.


def home(request):
    return render(request, "home.html")


def contacto(request):

    data = {
        "form_contacto": ContactoForm,
        "mensaje":""
    }
    formulario = ContactoForm(data=request.POST)

    if formulario.is_valid():
        formulario.save()
        data["mensaje"]= " Mensaje Enviado correctamente "
        return redirect(reverse("login")) 
    else:
        data["mensaje"]= "Rellene los campos indicados"
        data["form_contacto"] = formulario

    return render(request, "contacto.html", data)


@login_required(login_url='/accounts/login/')
def homeAdmin(request):
    return render(request, "homeAdmin.html")

@login_required(login_url='/accounts/login/')
def homeAlumno(request):
    return render(request, "homeAlumno.html")

def login_usuario(request):
    print("Bienvenido " + request.user.username)
    if request.user.groups.filter(name='alumno'):    
        return redirect(to='homeAlumno')
    else:   
        return redirect(to='homeAdmin')


def registroUsuarios(request):

    data={

        'form' : AlumnosForm
}

    if request.POST: 
        form = AlumnosForm(request.POST, request.FILES)
        if form.is_valid():
            rut = form.cleaned_data.get('rut_Usuario')
            nombre = form.cleaned_data.get('nombre_Usuario')
            apellido = form.cleaned_data.get('apellido_Usuario')
            telefono = form.cleaned_data.get('telefono_Usuario')
            carrera = form.cleaned_data.get('carrera_Usuario')
            semestre = form.cleaned_data.get('semestre_Usuario')
            correo = form.cleaned_data.get('correo')
            password = form.cleaned_data.get('password')

            if User.objects.filter(email=correo).exists():
                messages.error(request, "El correo ya se encuentra registrado.")

            else:
                usu = User()
                usu.set_password(password)
                usu.email = correo
                usu.username = nombre
                usu.first_name = nombre
                usu.last_name = apellido
                grupo = Group.objects.get(name='alumno')

                usu.save()

                alumno = Datos_Alumnos()
                alumno.rut_Usuario = rut
                alumno.nombre_Usuario = nombre
                alumno.apellido_Usuario = apellido
                alumno.telefono_Usuario = telefono
                alumno.carrera_Usuario = carrera
                alumno.semestre_Usuario = semestre
                alumno.correo = correo
                alumno.password = password  
                
                alumno.save()

                usu.groups.add(grupo)
                messages.success(request,"Usuario creado con éxito")
                return redirect(reverse("login"))    

    return render(request,"registration/registroUsuarios.html", data)


def inicioAdmin(request):
    return render(request,"baseAdmin.html")

def inicioAlumno(request):
    return render(request, "baseAlumno.html")