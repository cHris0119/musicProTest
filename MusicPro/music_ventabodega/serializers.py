from django.db.models.base import Model
from rest_framework import serializers
from music_pro.models import Bodega, Producto

class ProductoSerializador (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProd', 'nombre', 'precio', 'marca', 'categoria', 'img']
class stockSerializador (serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = ['stock']


