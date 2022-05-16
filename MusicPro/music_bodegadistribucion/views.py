from tkinter.tix import Tree
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from music_pro.models import Bodega, pedido, Producto
from .serializers import ProductoSerializador, PedidoSerializador, BodegaSerializador

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt

@api_view(['GET'])
def Consulta (request, cod):
    request.method == 'GET'
    a = Producto.objects.get( codigo = cod, tienda = 1)
    serializer = ProductoSerializador(a)
    return Response(serializer.data)
    

@api_view(['GET','POST'])
def pedir_ver_pedidos (request):
    if request.method == 'GET':
        a = pedido.objects.all()
        serializer = PedidoSerializador(a, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = PedidoSerializador(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def eliminarpedido(request,id):
    try:
        a = pedido.objects.get(idPedido = id)
    except pedido.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    request.method == 'DELETE'
    a.delete()
    return Response(status= status.HTTP_204_NO_CONTENT)