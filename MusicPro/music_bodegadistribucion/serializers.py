from django.db.models.base import Model
from rest_framework import serializers
from music_pro.models import  Bodega, pedido, Producto

class BodegaSerializador (serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = ['stock']

class PedidoSerializador (serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = ['idPedido','nomPedido', 'cantidad', 'idProducto', 'tienda']

class ProductoSerializador (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProd', 'nombre', 'precio', 'marca', 'categoria']

