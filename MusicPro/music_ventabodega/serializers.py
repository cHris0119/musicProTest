from django.db.models.base import Model
from rest_framework import serializers
from music_pro.models import Producto

class ProductoSerializador (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProd', 'nombre', 'stock', 'precio', 'codigo', 'marca', 'categoria']


