from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from transbank.common.options import WebpayOptions
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.integration_type import IntegrationType
from transbank.webpay.webpay_plus.transaction import Transaction
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_process
from django.shortcuts import redirect, render
from .models import Bodega, Categoria, Cliente, Marca, Producto, TipoUsuario
from music_pro.models import Carrito, CarritoPro
# Create your views here.


def inicio(request):
    return render(request,'music_pro/inicio.html')

def login(request):
    return render(request,'music_pro/login.html')

def registro(request):
    return render(request,'music_pro/registro.html')

def carrito(request, usu):
    cliente = Cliente.objects.get(email = usu)
    try:
        a = Carrito.objects.get(cliente = cliente)
    except Carrito.DoesNotExist:
        a = None
    
    if a == None:
        cat = Categoria.objects.all()
        mar = Marca.objects.all()
        contexto = {"marca": mar, "categoria":cat}
        return render(request,'music_pro/productos.html', contexto)
    else:
        tot = CarritoPro.objects.filter(carrito=a).aggregate(Sum('subtotal'))
        objs = CarritoPro.objects.filter(carrito=a)
        pro = Producto.objects.all()
        contexto = {"carr":objs, "prod":pro, "total":tot}
        return render(request,'music_pro/carrito.html', contexto)

    

def productos(request):
    cat = Categoria.objects.all()
    mar = Marca.objects.all()
    contexto = {"marca": mar, "categoria":cat}
    return render(request,'music_pro/productos.html', contexto)

def registrarUser(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    img = request.FILES['img_user']
    email = request.POST['email']
    contra = request.POST['contra']
    contra2 = request.POST['contra2']
    tipoUsu = TipoUsuario.objects.get(nomTipoUs = 'Cliente')
    clientes = Cliente.objects.all()
    for i in clientes:
        cli1 = i.email
        if email == cli1:
            messages.error(request,'El correo ya existe')
            return redirect('registro')
    if contra != contra2:
        
        messages.error(request,'Las contraseñas deben ser iguales')
        return redirect('registro')
    else:
        Cliente.objects.create(rutCli = rut, nombre = nombre, img = img, apellido = apellido, email = email, contra = contra, tipousuario = tipoUsu)
        User.objects.create_user(username =  email, password = contra)
        return redirect('login')


def iniciar_sesion(request):
    correo = request.POST['email']
    contra = request.POST['contra']
    user = authenticate(username = correo, password = contra)
    if user is not None:
        if user.is_active:
            login_process(request, user)
            return redirect('inicio')
        else:
            messages.error(request,'El usuario no esta activo')
    else:
        messages.error(request,'Correo o contraseña incorrectos')
        return redirect('login')

def log_out(request):
    logout(request)
    return redirect('login')

def pagar(request):
    a = Carrito.objects.get(idCarrito = 1)
    monto = a.total
    b = CarritoPro.objects.filter(carrito = a)
    buy_order="asdkajsdas"
    session_id = "asdasdasd"
    amount = 2000
    return_url = "http://127.0.0.1:8000/devuelta"
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
    resp = tx.create(buy_order, session_id,  monto, return_url)
    url = resp['url']
    token = resp['token']

    contexto = {"ur": url, "tok":token, "carrito": b, "total":a}
    return render(request,'music_pro/pago.html', contexto)

def devueltapagar (request):
    token = request.GET['token_ws']
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
    response = tx.commit(token)
    vci = response['vci']
    amount = response['amount']
    status= response['status']
    orden = response['buy_order']
    session = response['session_id']
    cuenta = response['accounting_date']
    fecha = response['transaction_date']
    codigo = response['authorization_code']
    typocode = response['payment_type_code']
    respon = response['response_code']
    number = response['installments_number']
    contexto = {"amoun": amount, "stado": status, "orde": orden, "fech": fecha, "type": typocode, "cod": codigo, "count": cuenta}
    return render(request, 'music_pro/devuelta.html', contexto)


    
def consultadistribucion (request):

    return render(request, 'music_pro/con_distribucion.html')

def ver_eliminar_ped (request):

    return render(request, 'music_pro/ver_eliminar_pedido.html')

def inicioadm (request):

    return render(request, 'music_pro/inicioadm.html')

def consulta_ven (request):

    return render(request, 'music_pro/consulta_ven.html')



def agregarcarrito(request):
    precio = request.GET['precio']
    cantidad = request.GET['cantidad']
    usu = request.GET['usuario']
    id = request.GET['id_pro']
    ob2 = Producto.objects.get(idProd = id)
    bod = Bodega.objects.get(tienda = 2, producto = ob2)
    prec = int(precio)
    cant = int(cantidad)
    subtotal = prec*cant
    cli = Cliente.objects.get(email = usu)
    try:
        a = Carrito.objects.get(cliente = cli)
    except Carrito.DoesNotExist:
        a = None
    
    if a == None:
        nuevocarro = Carrito.objects.create(total= subtotal, fechaCarrito = '2022-06-16', cliente = cli)
        CarritoPro.objects.create(cantidad=cantidad, precioUnidad = precio, subtotal= subtotal, carrito=nuevocarro, producto=ob2)
        bod.stock = bod.stock - cant
        bod.save()
    else:
        try:
            obj = CarritoPro.objects.get(producto = ob2)
        except CarritoPro.DoesNotExist:
            obj=None
        if obj == None:
            CarritoPro.objects.create(cantidad=cantidad, precioUnidad = precio, subtotal= subtotal, carrito=a, producto=ob2)
            bod.stock = bod.stock - cant
            bod.save()
        else:
            bod.stock = bod.stock - cant
            bod.save()
            objcan = obj.cantidad
            can2 = cant+objcan
            subt =  prec*can2
            obj.cantidad = can2
            obj.subtotal = subt
            obj.save()
    return redirect('productos')


def Agregarusuario (request):
    Tius = TipoUsuario.objects.all()
    contexto = {"tipous": Tius}
    return render(request, 'music_pro/agregaruser.html', contexto)

def agregarus(request):
    tipous = request.POST['TipoDeUsuario']
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    img = request.FILES['img_user']
    email = request.POST['email']
    contra = request.POST['contra']
    contra2 = request.POST['contra2']
    tipoUsu = TipoUsuario.objects.get(idTipoUs = tipous)
    clientes = Cliente.objects.all()
    for i in clientes:
        cli1 = i.email
        if email == cli1:
            messages.error(request,'El correo ya existe')
            return redirect('agregarusuario')
    if contra != contra2:
        
        messages.error(request,'Las contraseñas deben ser iguales')
        return redirect('agregarusuario')
    else:
        Cliente.objects.create(rutCli = rut, nombre = nombre, img = img, apellido = apellido, email = email, contra = contra, tipousuario = tipoUsu)
        if tipoUsu.idTipoUs == 1:
            User.objects.create_user(username =  email, password = contra)
        elif tipoUsu.idTipoUs == 2:
            User.objects.create_user(username =  email, password = contra, is_staff=1, is_superuser=1)
        elif tipoUsu.idTipoUs == 3:
            User.objects.create_user(username =  email, password = contra, is_staff=1, is_superuser=0)
        else:
            User.objects.create_user(username =  email, password = contra, is_staff=0, is_superuser=1)
        return redirect('inicioadm')