from django.contrib import admin
from django.urls import path
from .views import consultadistribucion, devueltapagar, pagar, inicio, login, registro, carrito, productos,registrarUser, iniciar_sesion, log_out, ver_eliminar_ped

urlpatterns = [
    path('', inicio, name="inicio"),
    path('pagar', pagar, name="pagar"),
    path('devuelta', devueltapagar, name="devuelta"),
    path('login', login, name="login"),
    path('registro', registro, name="registro"),
    path('carrito', carrito, name="carrito"),
    path('productos', productos, name="productos"),
    path('registrarUser', registrarUser, name="registrarUser"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('log_out', log_out, name="log_out"),
     path('consulta_distribucion', consultadistribucion, name="consulta_distribucion"),
    path('ver_eliminar_ped', ver_eliminar_ped, name="ver_eliminar_ped"),
    ]