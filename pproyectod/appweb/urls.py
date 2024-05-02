from django.urls import path
from .views import *
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('home/',home, name="home" ),
    path('contacto/', contacto , name="contacto" ),
    path('homeAdmin/', homeAdmin ,name="homeAdmin"),
    path('login_usuario/' , login_usuario , name="login_usuario"),
    path('registroUsuarios/',registroUsuarios, name="registroUsuarios"),
    path('homeAlumno/', homeAlumno ,name="homeAlumno"),
    path('registroUsuariosAdmin/', registroUsuariosAdmin ,name="registroUsuariosAdmin"),
    path('homeModerador/', homeModerador , name="homeModerador"),
    path('postAlumno/', postAlumnos , name="postAlumno"),
    path('publicaciones/', publicaciones , name="publicaciones"),

    path('listarAlumnos/', listarAlumnos, name="listarAlumnos"),
    path('modificarAlumno/<rut_Usuario>',modificarAlumno,name='modificarAlumno'),
    path('eliminar_usuario/<rut_Usuario>/', eliminar_usuario, name="eliminar_usuario"),
    
    path('listarModerador/', listarModerador, name="listarModerador"),
    path('modificarModerador/<rut_Moderador>',modificarModerador,name='modificarModerador'),
    path('eliminar_moderador/<rut_Moderador>/', eliminar_moderador, name="eliminar_moderador"),
]
