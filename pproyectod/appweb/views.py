from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, "home.html")


def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse("login")) 
        else:
            mensaje_error = "Por favor, corrija los errores en el formulario."
            return render(request, "contacto.html", {"form_contacto": formulario, "mensaje": mensaje_error})
    else:
        formulario = ContactoForm()
        return render(request, "contacto.html", {"form_contacto": formulario})


@login_required(login_url='/accounts/login/')
def homeAdmin(request):
    return render(request, "homeAdmin.html")

@login_required(login_url='/accounts/login/')
def homeAlumno(request):
    return render(request, "homeAlumno.html")

def login_usuario(request):
    username = request.user.username
    print("Bienvenido " + username)
    
    # Mostrar SweetAlert según el tipo de usuario
    if request.user.groups.filter(name='alumno').exists():
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como alumno.')
    elif request.user.groups.filter(name='moderador').exists():
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como moderador.')
    else:
        messages.success(request, f'Bienvenido {username}. Sesión iniciada como administrador.')

    # Redirigir al usuario a la página de inicio correspondiente
    if request.user.groups.filter(name='alumno').exists():
        return redirect('homeAlumno')
    elif request.user.groups.filter(name='moderador').exists():
        return redirect('homeModerador')
    else:
        return redirect('homeAdmin')
        


def registroUsuarios(request):
    data = {'formAl': AlumnosForm}

    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirmar_password = form.cleaned_data.get('confirmar_password')

            if password != confirmar_password:
                messages.error(request, "Las contraseñas no coinciden.")
                return render(request, 'registration/registroUsuarios.html', data)
            else:
                rut = form.cleaned_data.get('rut_Usuario')
                nombre = form.cleaned_data.get('nombre_Usuario')
                apellido = form.cleaned_data.get('apellido_Usuario')
                telefono = form.cleaned_data.get('telefono_Usuario')
                carrera = form.cleaned_data.get('carrera_Usuario')
                semestre = form.cleaned_data.get('semestre_Usuario')
                correo = form.cleaned_data.get('correo')

                if User.objects.filter(email=correo).exists():
                    messages.error(request, "El correo ya se encuentra registrado.")
                    return render(request, 'registration/registroUsuarios.html', data)
                else:
                    usu = User.objects.create_user(username=nombre, email=correo, password=password, first_name=nombre, last_name=apellido)
                    grupo = Group.objects.get(name='alumno')
                    usu.groups.add(grupo)

                    alumno = Datos_Alumnos.objects.create(
                        rut_Usuario=rut,
                        nombre_Usuario=nombre,
                        apellido_Usuario=apellido,
                        telefono_Usuario=telefono,
                        carrera_Usuario=carrera,
                        semestre_Usuario=semestre,
                        correo=correo,
                        password=password
                    )
                    messages.success(request, "Usuario creado con éxito")
                    return redirect(reverse("login"))

    return render(request, "registration/registroUsuarios.html", data)


@login_required(login_url='/accounts/login/')
def inicioAdmin(request):
    return render(request,"baseAdmin.html")


@login_required(login_url='/accounts/login/')
def inicioAlumno(request):
    return render(request, "baseAlumno.html")



@login_required(login_url='/accounts/login/')
def inicioModerador(request):
    return render(request, "baseModerador.html")

@login_required(login_url='/accounts/login/')
def homeModerador(request):
    return render(request, "homeModerador.html")

@login_required(login_url='/accounts/login/')
def registroUsuariosAdmin(request):
    data = {'formModerador': ModeradorForm}

    if request.method == 'POST':
        form = ModeradorForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirmar_password = form.cleaned_data.get('confirmar_password')

            if password != confirmar_password:
                messages.error(request, "Las contraseñas no coinciden.")
                return render(request, 'registration/registroUsuarios.html', data)
            else:
                nombre_moderador = form.cleaned_data.get('nombre_Moderador')
                apellido_moderador = form.cleaned_data.get('apellido_Moderador')  # Obtener el apellido del formulario
                rut_moderador = form.cleaned_data.get('rut_Moderador')
                telefono_Moderador = form.cleaned_data.get('telefono_Moderador')
                correo = form.cleaned_data.get('correo')

                if User.objects.filter(email=correo).exists():
                    messages.error(request, "El correo ya se encuentra registrado.")
                    return render(request, 'registration/registroUsuarios.html', data)
                else:
                    usu = User.objects.create_user(username=nombre_moderador, email=correo, password=password, first_name=nombre_moderador, last_name=apellido_moderador)
                    grupo = Group.objects.get(name='moderador')
                    usu.groups.add(grupo)

                    moderador = form.save()  # Guardar el moderador en la base de datos

                    messages.success(request, "Usuario creado con éxito")
                    return redirect(reverse("homeAdmin"))

    return render(request, "mantenedor/registroUsuariosAdmin.html", data)


@login_required(login_url='/accounts/login/')
def postAlumnos(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Publicación subida con éxito!')
            return redirect('homeAlumno')
        else:
            messages.error(request, '¡Ha ocurrido un error al subir la publicación!')
    else:
        form = PublicacionForm()

    data = {
        'formPost': form,
    }
    return render(request, "postAlumno.html", data)


@login_required(login_url='/accounts/login/')
def publicaciones(request):
    queryset = request.GET.get("buscar")
    
    if queryset:
        publicaciones = PostAlumnos.objects.filter(
            Q(nombre_post__icontains=queryset) |
            Q(descripcion_post__icontains=queryset)
        ).distinct()
        mensaje = None  # Reinicia el mensaje a None ya que hay resultados de búsqueda
    else:
        publicaciones = PostAlumnos.objects.all()  # Mostrar todas las publicaciones
        mensaje = "No se encontraron publicaciones con esa búsqueda."

    data = {
        "publicaciones": publicaciones,
        "mensaje": mensaje
    }

    return render(request, "publicaciones.html", data)

@login_required(login_url='/accounts/login/')
def listarAlumnos(request):

    usuairos = Datos_Alumnos.objects.all()

    data={
        'usuarios': usuairos
    }
    return render(request, "mantenedor/listarAlumnos.html", data)



@login_required(login_url='/accounts/login/')
def eliminar_usuario(request, rut_Usuario):
    datos_usuarios = get_object_or_404(Datos_Alumnos, rut_Usuario=rut_Usuario)

    datos_usuarios.delete()
    messages.success(request, "El rut del usuario es : "+ rut_Usuario + " fue eliminado correctamente")

    return redirect(to="listarAlumnos")




@login_required(login_url='/accounts/login/')
def modificarAlumno(request, rut_Usuario):

    datos_usuario = get_object_or_404(Datos_Alumnos, rut_Usuario=rut_Usuario)

    data = {
        "formA": AlumnosForm(instance=datos_usuario)
    }

    if request.method == 'POST':
        formulario = AlumnosForm(data=request.POST, files=request.FILES, instance=datos_usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarAlumnos")
        else:
            data["mensaje"] = "Hubo un error"
            data["formA"] =  formulario


    return render(request, "mantenedor/modificarAlumno.html", data)


@login_required(login_url='/accounts/login/')
def listarModerador(request):

    moderador = Datos_Moderador.objects.all()

    data={
        'moderador': moderador
    }
    return render(request, "mantenedor/listarModerador.html", data)


@login_required(login_url='/accounts/login/')
def modificarModerador(request, rut_Moderador):

    datos_moderador = get_object_or_404(Datos_Moderador, rut_Moderador=rut_Moderador)

    data = {
        "formMo": ModeradorForm(instance=datos_moderador)
    }

    if request.method == 'POST':
        formulario = ModeradorForm(data=request.POST, files=request.FILES, instance=datos_moderador)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarModerador")
        else:
            data["mensaje"] = "Hubo un error"
            data["formMo"] =  formulario


    return render(request, "mantenedor/modificarModerador.html", data)

@login_required(login_url='/accounts/login/')
def eliminar_moderador(request, rut_Moderador):
    datos_moderador = get_object_or_404(Datos_Moderador, rut_Moderador=rut_Moderador)

    datos_moderador.delete()
    messages.success(request, "El rut del usuario es : "+ rut_Moderador + " fue eliminado correctamente")

    return redirect(to="listarModerador")