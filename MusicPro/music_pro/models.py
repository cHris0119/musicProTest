from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

# Create your models here.

class  Region (models.Model):
    idRegion = models.AutoField (primary_key=True, verbose_name="id de la region")
    nomRegion = models.CharField(max_length= 20, verbose_name="nombre de la region")
 
    def __str__(self):
        return self.nomRegion

class Comuna (models.Model):
    idComuna = models.AutoField(primary_key=True, verbose_name="Identificador de comuna")
    nomComuna= models.CharField(max_length=20, verbose_name="Nombre de la comuna")

    def __str__(self):
        return self.nomComuna

class TipoUsuario (models.Model):
    idTipoUs = models.AutoField(primary_key=True, verbose_name="Identificadot del tipo de usuario")
    nomTipoUs = models.CharField(max_length=30, verbose_name="Tipo de usuario establecido")

    def __str__(self):
        return self.nomTipoUs

class Cliente (models.Model):
    rutCli = models.CharField(primary_key=True, max_length=14, verbose_name="Run del usuario")
    nombre = models.CharField(max_length=20, verbose_name="nombre o nombres del usuario")
    img = models.ImageField(upload_to="img_mp", null=True)
    apellido = models.CharField(max_length=20, verbose_name="apellido o apellidos del usuario")
    email = models.CharField(max_length=50, verbose_name="Email del usuario")
    contra = models.CharField(max_length=12, verbose_name="contraseña del usuario")
    tipousuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Direccion (models.Model):
    idDireccion = models.AutoField(primary_key=True, verbose_name="identificador de la direccion")
    domicilio = models.CharField(max_length=40, verbose_name="direccion del domicilio")
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__ (self):
        return self.domicilio

class Carrito (models.Model):
    idCarrito = models.AutoField(primary_key=True, verbose_name="identificador unico del carrito")
    total = models.IntegerField(verbose_name="total del carrito")
    fechaCarrito = models.DateField(verbose_name="fecha del carrito")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Marca (models.Model):
    idMarca = models.AutoField(primary_key=True, verbose_name="identificador unico de la marca")
    nombreMarca = models.CharField(max_length=20, verbose_name="Nombre de la marca")

    def __str__ (self):
        return self.nombreMarca

class Categoria (models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name="Identificador de la categoria")
    nombreCategoria = models.CharField(max_length=25, verbose_name="nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Tienda (models.Model):
    idTienda = models.AutoField(primary_key=True, verbose_name="Identificador unico de la tienda")
    direccion = models.CharField(max_length=30, verbose_name="direccion de la tienda")

    def __str__(self):
        return self.direccion

class Producto (models.Model):
    idProd = models.AutoField (primary_key=True, verbose_name="identificador unico del producto")
    nombre = models.CharField(max_length=30, verbose_name="nombre del producto")
    img = models.ImageField(upload_to="img_mp", null=True)
    precio = models.IntegerField(verbose_name="precio unitario del producti")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CarritoPro (models.Model):
    idCarritoPro = models.AutoField(primary_key=True, verbose_name="identificador de carrito clase intermedia")
    cantidad = models.IntegerField(verbose_name="cantidad de unidades del producto pedido")
    precioUnidad = models.IntegerField(verbose_name="precio unitario del producto")
    subtotal = models.IntegerField(verbose_name="la multiplicacion del precio unitario con la cantidad de productos solicitados")
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Bodega (models.Model):
    idBodega = models.AutoField(primary_key=True, verbose_name="identificador de la bodega")
    stock = models.IntegerField(verbose_name="cantidad del producto", default=0)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class pedido (models.Model):
    idPedido = models.AutoField(primary_key=True, verbose_name="id del pedido realizado por la bodega a la empresa")
    nomPedido = models.CharField(max_length=20, verbose_name="nombre del producto pedido")
    cantidad = models.IntegerField(verbose_name="cantidad del producto solicitado")
    codigoProducto = models.CharField(max_length=5, verbose_name=" 2 letras 3 numeros ej: LS123")
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomPedido

class HistorialVentas (models.Model):
    idHistorial = models.AutoField (primary_key=True, verbose_name="identifiador del historial")
    total = models.IntegerField (verbose_name="total de la venta realizada")
    fecha = models.DateField (verbose_name="fecha de la venta realizada")
    run = models.CharField(max_length=14, verbose_name="rut del usuario que realizo la compra")
    tienda = models.ForeignKey (Tienda, on_delete=models.CASCADE)
