from array import typecodes
from dataclasses import dataclass
import email
from urllib import response
from django.contrib import messages
from urllib.request import Request
from django.contrib.auth.models import User
from django.test import TransactionTestCase
import requests
from transbank.common.options import WebpayOptions
from transbank.common.request_service import RequestService
from transbank.common.api_constants import ApiConstants
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.integration_type import IntegrationType
from transbank.common.validation_util import ValidationUtil
from transbank.common.webpay_transaction import WebpayTransaction
from transbank.webpay.webpay_plus.schema import TransactionCreateRequestSchema, TransactionRefundRequestSchema, TransactionCaptureRequestSchema
from transbank.webpay.webpay_plus.request import TransactionCreateRequest, TransactionRefundRequest, TransactionCaptureRequest
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.error.transbank_error import TransbankError
from transbank.error.transaction_create_error import TransactionCreateError
from transbank.error.transaction_commit_error import TransactionCommitError
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.error.transaction_capture_error import TransactionCaptureError
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_process
import urllib, json


from django.shortcuts import redirect, render
from .models import Cliente, TipoUsuario

from music_pro.models import Carrito, CarritoPro
#from transbank.common.options import WebpayOptions
#from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
#from transbank.common.integration_api_keys import IntegrationApiKeys
#from transbank.common.integration_type import IntegrationType
# Create your views here.


def inicio(request):
    return render(request,'music_pro/inicio.html')

def login(request):
    return render(request,'music_pro/login.html')

def registro(request):
    return render(request,'music_pro/registro.html')

def carrito(request):
    return render(request,'music_pro/carrito.html')

def productos(request):
    return render(request,'music_pro/productos.html')

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


    
