import imp
from unittest.util import _MAX_LENGTH
from django.db import models
import email
import enum
from email.policy import default
from enum import unique
from operator import truediv
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


class Proyecto(models.Model):
    name = models.CharField(max_length = 200)
    document = models.CharField(max_length = 200)
    email = models.EmailField(null = True, blank = True)

    def __str__(self):
        return "%s the name" % self.name


class monedas(models.Model):
    tasa = models.FloatField(max_length = 200)
    moneda = models.CharField(max_length = 45)
    habilitar = models.BooleanField(default = True)
    codigomoneda = models.CharField(max_length = 45, primary_key = True)

    def __str__(self):
        return self.moneda


class transaccion(models.Model):
    monto = models.BigIntegerField
    fecha = models.DateField
    email = models.CharField(max_length = 45, primary_key = True)

    def __str__(self):
        return "%s the user_registered" % self.monto


class Destinatarios(models.Model):
    documento = models.BigIntegerField
    tipodocumento = models.CharField(max_length = 200, default = 'cc')
    email = models.CharField(max_length = 200, primary_key = True)

    def __str__(self):
        return  self.documento


class Usuario_registrado(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    #usuario.id = models.Model.ForeignKey(User, on_delete=models.CASCADE)
    documento = models.BigIntegerField()
    direccion = models.CharField(max_length = 200)
    email = User.email, models.ForeignKey(transaccion, on_delete = models.CASCADE)
    email2 = User.email, models.ForeignKey(Destinatarios, on_delete = models.CASCADE)
    monedas = models.ForeignKey(monedas, on_delete = models.CASCADE, null = True)
    pais = models.CharField(max_length = 45)
    ciudad = models.CharField(max_length = 45)
    tipodocumento = models.CharField(max_length = 45)
    fechaexpedicion = models.DateField(max_length = 20)
    dinero = models.DecimalField(decimal_places = 3, max_digits = 10, default = 0)
    celular = models.BigIntegerField()
    #def __str__(self):
        #return "%s the user_registered" % self.documento

