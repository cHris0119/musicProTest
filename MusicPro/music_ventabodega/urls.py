from django.urls import path
from .views import traerTodosProductos, traerUnProducto, traerUnaCategoria, traerUnaMarca
from .viewslogin import login

urlpatterns = [
    path('Productos', traerTodosProductos ,name="Productos"),
    path('Marca/<idm>', traerUnaMarca ,name="Marca"),
    path('Categoria/<idc>', traerUnaCategoria ,name="Categoria"),
    path('Producto/<id>', traerUnProducto ,name="Producto"),
    path('loginRest',login,name="loginRest"),
]