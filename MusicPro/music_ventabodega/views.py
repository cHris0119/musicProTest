from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from music_pro.models import Categoria, Producto, Bodega, pedido
from .serializers import  ProductoSerializador, stockSerializador

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt

@api_view(['GET'])
def traerTodosProductos (request):
    request.method == 'GET'
    a = Producto.objects.filter(tienda = 2)
    serializer = ProductoSerializador(a, many = True)
    return Response(serializer.data)
       

@api_view(['GET'])
def traerUnProducto(request,id):
    try: 
        b = Bodega.objects.get(tienda = 2, producto = id)
    except Bodega.DoesNotExist:
        b = None
    if b is None:
        return Response(status= status.HTTP_404_NOT_FOUND)
    else:
        a = Producto.objects.get(idProd = id)
        
    request.method == 'GET'
    serializer = stockSerializador(a)
    return Response(serializer.data)

@api_view(['GET'])
def traerUnaCategoria(request,idc):
    a = Producto.objects.filter(categoria = idc, tienda=2)
    request.method == 'GET'
    serializer = ProductoSerializador(a, many = True) 
    return Response(serializer.data)

@api_view(['GET'])
def traerUnaMarca(request,idm):
    try:
        a = Producto.objects.filter(marca = idm, tienda =2)
    except Producto.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    request.method == 'GET'
    serializer = ProductoSerializador(a, many = True)
    return Response(serializer.data)

    