from msilib.schema import Class
from operator import ge
from urllib import response
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from music_pro.models import Producto, Marca, Categoria, Tienda, Bodega


class testVentaBodega(TestCase):

    def setUp(self):
        Tienda.objects.create(
            idTienda=2,
            direccion='callefalsa123'
        )

        Marca.objects.create(
            idMarca=1,
            nombreMarca='casio'
        )

        Categoria.objects.create(
            idCategoria=1,
            nombreCategoria='guitarra'
        )

        Producto.objects.create(
            idProd=1,
            nombre='Guitarra1',
            precio=100,
            marca=Marca.objects.get(idMarca=1, nombreMarca='casio'),
            categoria=Categoria.objects.get(idCategoria=1, nombreCategoria='guitarra'))

        Producto.objects.create(
            idProd=2,
            nombre='Guitarra2',
            precio=100,
            marca=Marca.objects.get(idMarca=1, nombreMarca='casio'),
            categoria=Categoria.objects.get(idCategoria=1, nombreCategoria='guitarra'))

        Bodega.objects.create(
            idBodega=1,
            stock=20,
            tienda=Tienda.objects.get(idTienda=2, direccion='callefalsa123'),
            producto=Producto.objects.get(idProd=1, nombre='Guitarra1', precio=100,
            marca=Marca.objects.get(idMarca=1, nombreMarca='casio'),
            categoria=Categoria.objects.get(idCategoria=1, nombreCategoria='guitarra'))

        )

    def test_ObtenerProductos(self):
        url = "/api_VentaBodega/Productos"
        response = self.client.get(url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['nombre'], "Guitarra1")

    def test_ObtenerProductoMarca(self):
        url = "/api_VentaBodega/Marca/1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_ObtenerProductoMarcaMalo(self):
        url = "/api_VentaBodega/Marca/100"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


    def test_ObtenerProductoCate(self):
        url = "/api_VentaBodega/Categoria/1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_ObtenerProductoCateMalo(self):
        url = "/api_VentaBodega/Categoria/100"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


    def test_ObtenerProductoid(self):
        url = "/api_VentaBodega/Producto/1"
        response = self.client.get(url)
     
        self.assertEqual(response.status_code, 200)

    def test_ObtenerProductoidMalo(self):
        url = "/api_VentaBodega/Producto/5"
        response = self.client.get(url)
     
        self.assertEqual(response.status_code, 404)