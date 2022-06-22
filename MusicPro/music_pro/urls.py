from django.contrib import admin
from django.urls import path
from .views import Agregarusuario, agregarcarrito, agregarus, consultadistribucion, devueltapagar, hacerped, pagar, inicio, login, pedido, registro, carrito, productos,registrarUser, iniciar_sesion, log_out, ver_eliminar_ped, inicioadm,consulta_ven

from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('home', login_required(inicio), name="inicio"),
    path('pagar', pagar, name="pagar"),
    path('devuelta', devueltapagar, name="devuelta"),
    path('', login, name="login"),
    path('registro', registro, name="registro"),
    path('carrito/<str:usu>',  login_required(carrito), name="carrito"),
    path('productos',  login_required(productos), name="productos"),
    path('registrarUser', registrarUser, name="registrarUser"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('log_out', log_out, name="log_out"),
    path('consulta_distribucion',  login_required(consultadistribucion), name="consulta_distribucion"),
    path('ver_eliminar_ped',  login_required(ver_eliminar_ped), name="ver_eliminar_ped"),
    path('inicioadm',  login_required(inicioadm), name="inicioadm"),
    path('consulta_ven',  login_required(consulta_ven), name="consulta_ven"),

    path('agregarcarrito', login_required(agregarcarrito), name="agregarcarrito"),
    path('agregarusuario', login_required(Agregarusuario), name="agregarusuario"),
    path('agregarus', login_required(agregarus), name="agregarus"),
    path('hacerpedido', login_required(hacerped), name="hacerpedido"),
    path('pedido', login_required(pedido), name="pedido"),
    ]