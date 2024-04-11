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
]