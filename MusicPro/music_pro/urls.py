from django.contrib import admin
from django.urls import path
from .views import devueltapagar, home, pagar

urlpatterns = [
    path('', home, name="home"),
    path('pagar', pagar, name="pagar"),
    path('devuelta', devueltapagar, name="devuelta")
    ]