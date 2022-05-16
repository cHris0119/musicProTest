from array import typecodes
from urllib.request import Request
from django.test import TransactionTestCase
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


from django.shortcuts import render

from music_pro.models import Carrito, CarritoPro
#from transbank.common.options import WebpayOptions
#from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
#from transbank.common.integration_api_keys import IntegrationApiKeys
#from transbank.common.integration_type import IntegrationType
# Create your views here.


def home(request):

    return render(request,'music_pro/home.html')

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
    