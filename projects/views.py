from faulthandler import cancel_dump_traceback_later
from django.shortcuts import render
from django.http import HttpResponse
from enum import auto
from inspect import Attribute
import re
import datetime
from xml.dom.minidom import Document
from decimal import Decimal
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import F
from django.contrib.auth.hashers import make_password

def trukea(request):
    return render(request, 'index.html')

def EnviarDinero(request):
    return render(request, 'enviar_dinero.html')

def ClienteTransaccion(request):
    return render(request, 'cliente_transaccion.html')


def CrearCuenta(request):
    listamonedas = monedas.objects.all()
    print(listamonedas)
    contexto = {'listamonedas':listamonedas}
    return render(request, 'crear_cuenta.html', contexto)


def InicioCliente(request):
    template = 'inicio_cliente.html'
    print(request.user.id)
    user_data = models.Usuario_registrado.objects.get(usuario = request.user.id)
    return render(request, 'inicio_cliente.html', {'user_data':user_data})



def AgregarDestinatario(request):
    if request.method == 'POST':    
        username = request.POST['email']
        email = request.POST['email']
        documento = request.POST['documento']
        tipodocumento = request.POST['tipodocumento']
        user = models.Destinatarios()
        user.email = email
        user.documento = documento
        user.tipodocumento = tipodocumento
        user.save()

        if User.objects.filter(username = username).exists():
           user2 = User.objects.filter(username = email).values_list('first_name', 'last_name')
           firstname = user2[0][0]
           lastname = user2[0][1]
           contexto = {'nombre':firstname, 'apellido':lastname}
           return render(request, 'notificacion_agregar_destinatario.html', contexto)
        else:
            return HttpResponse("Error: El usuario no existe")

    return render(request,'agregar_destinatario.html')


def ClienteTransaccion(request):
    return render(request, 'cliente_transaccion.html')


def RecuperarContrasena(request):
    return render(request, 'recuperar_contrasena.html')


def EnviarDinero(request):
    destinatarios = models.Destinatarios.objects.all()
    contexto = {'destinatarios':destinatarios}

    if request.method == 'POST':
        print('entra')
        dinero = request.POST['monto']
        fecha = request.POST['fecha']
        email = request.POST['email']

        if models.Destinatarios.objects.filter(email = email).exists():
            transaccion = models.transaccion()
            transaccion.monto = dinero
            transaccion.fecha = fecha
            transaccion.email = email
            #transaccion.save()
            user2 = User.objects.filter(username = email).values_list('first_name', 'last_name', 'username')
            firstname = user2[0][0]
            lastname = user2[0][1]
            correo = user2[0][2]
            user_moneda = models.Usuario_registrado.objects.filter(username = email).values_list('monedas')
            print(user_moneda)
            contexto2 = {'firstname':firstname, 'lastname':lastname, 'correo':correo, 'monto local':dinero}
        else: 
            HttpResponse('El usuario al que intenta enviar dinero no esta en la lista de Destinatarios')
   
    return render(request, 'enviar_dinero.html', contexto,contexto2)


def AgregarDinero(request):
    if request.method == 'POST':
        dinero = request.POST['monto']
        user_data = models.Usuario_registrado.objects.get(usuario = request.user.id)
        user_data.dinero += Decimal(dinero)
        user_data.save()
    
    return render(request, 'agregar_dinero.html')


def EliminarDestinatario(request):
    return render(request, 'eliminar_destinatario.html')

def InicioAdministrador(request):
    return render(request, 'inicio_administrador.html')

def HabilitarDeshabilitarMoneda(request):
    return render(request, 'habilitar_deshabilitar_moneda.html')

def ConsultarListaTransacciones(request):
    return render(request, 'consultar_lista_transacciones.html')

def EditarMoneda(request):
    return render(request, 'editar_moneda.html')

def AdminEditarMoneda(request):
    return render(request, 'admin_editar_moneda.html')


def AgregarMonedaPlataforma(request):
    moneda = None
    tasa = None
    codigomoneda = None

    if request.method == 'POST':
        print(request.POST)
        tasa = request.POST['tasa']
        moneda = request.POST['moneda']
        codigomoneda = request.POST['codigomoneda']
        user3 = models.monedas()
        user3.moneda = moneda
        user3.tasa = tasa
        user3.codigomoneda = codigomoneda
        user3.save()

    return render(request, 'agregar_moneda_plataforma.html')


def ConsultarListaMonedas(request):
    listatasa = models.monedas.objects.values_list('tasa')
    listamoneda = models.monedas.objects.values_list('moneda')
    listacodigo = models.monedas.objects.values_list('codigomoneda')
    listatotal =  models.monedas.objects.values()
    contexto = {'listatasa':listatasa, 'listamoneda':listamoneda, 'listacodigo':listacodigo, 'listatotal':listatotal}
    return render(request, 'consultar_lista_monedas.html', contexto)


def ClienteLIstaTransacciones(request):
    return render(request, 'cliente_lista_transacciones.html')


def projects(request):
    proyectos = models.Proyecto.objects.all()
    Usuario_reg = models.Usuario_registrado.objects.all()
    Users_orig = models.User.objects.all()
    Add_coin = models.Agregar_moneda.objects.all()
    return render(request, 'projects.html', {'proyectos':proyectos, 'Usuario_reg':Usuario_reg,
    'Users_orig':Users_orig, 'Add_coin':Add_coin})


@login_required(login_url = 'login')
def project(request):
    return render(request, 'single-project.html')


def crearcuenta(request):
    if request.method == 'POST':    
        username = request.POST['email']
        password = make_password(request.POST['password'])
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        documento = request.POST['documento']
        monedas = request.POST['monedas']
        celular = request.POST['celular']
        ciudad = request.POST['ciudad']
        fechaexpedicion = request.POST['fechaexpedicion']
        pais = request.POST['pais']
        direccion = request.POST['direccion'] 
        tipodocumento = request.POST['tipodocumento']
        datos = request.POST
        print(datos)

        if User.objects.filter(username = username).exists():
            return HttpResponse("Error: El nombre de usuario ya existe")
        elif User.objects.filter(email = email).exists():
            return HttpResponse("Error: El correo ya existe")
        else:  
            user = User()
            user.is_active = 1
            user.username = email
            user.password = password
            user.email = email
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            user2 = models.Usuario_registrado()
            user2.usuario = user
            user2.documento = documento
            user2.monedas = monedas
            user2.celular = celular
            user2.ciudad = ciudad
            user2.fechaexpedicion = fechaexpedicion
            user2.pais = pais
            user2.tipodocumento = tipodocumento
            user2.save()

    listamonedas = models.monedas.objects.all()
    print(listamonedas)
    contexto = {'listamonedas':listamonedas}
    return render(request, 'crear_cuenta.html', contexto)
    

def IniciarSesion(request):

    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        try:
           user = User.objects.get(username=username)
        except:
            return HttpResponse("Error: el usuario no existe")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        if  username == 'valen@gmail.com':
                return redirect('InicioCliente')
        else:
                return redirect('InicioCliente')
                HttpResponse("Error: Usuario o contraseña incorrecta")
    
    return render(request, 'iniciar_sesion.html')


def mainPage(request):
    return render(request, 'main.html')


def CerrarSesion(request):
    logout(request)
    return HttpResponse("Logout Correcto")


def monedas(request):
    if request.user.is_superuser:
        return('projects')

    if request.method == 'POST':
        tasa = request.POST['tasa']
        moneda = request.POST['moneda']
        codigomoneda = request.POST['Codigo de la moneda']
    else:
        user3 = models.monedas()
        user3.moneda = moneda
        user3.tasa = tasa
        user3.codigomoneda = codigomoneda
        user3.save()
        
    return render(request, 'iniciar_sesion.html')

