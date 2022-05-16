from django.contrib import admin
from .models import Bodega, Region, Comuna, TipoUsuario, Cliente, Direccion, Carrito,Marca, CarritoPro, Categoria, Producto, Tienda, pedido, HistorialVentas

# Register your models here.

admin.site.register(Bodega)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Cliente)
admin.site.register(TipoUsuario)
admin.site.register(Direccion)
admin.site.register(Carrito)
admin.site.register(Marca)
admin.site.register(CarritoPro)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(pedido)
admin.site.register(HistorialVentas)