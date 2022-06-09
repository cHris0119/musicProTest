from django.urls import path
from .views import Consulta, eliminarpedido, pedir_ver_pedidos
from .viewslogin import login

urlpatterns = [
    path('Consultar/<int:id>', Consulta ,name="Consulta"),
    path('Ver_Pedir', pedir_ver_pedidos, name ="ver_pedir"),
    path('eliminar_pedido/<int:id>', eliminarpedido, name="eliminarpedido" ),
    path('loginRest',login,name="loginRest"),
]