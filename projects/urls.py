from django.urls import path
from . import views

urlpatterns = [

    # Vistas inicio
    path('trukea/', views.trukea,name="trukea"),
    path('iniciar_sesion/', views.IniciarSesion,name="iniciar_sesion"),
    path('CerrarSesion/', views.CerrarSesion,name="CerrarSesion"),
    path('CrearCuenta/', views.crearcuenta,name="CrearCuenta"),

    # Vistas administrador
    path('InicioAdministrador/', views.InicioAdministrador,name="InicioAdministrador"),
    path('ConsultarListaMonedas/', views.ConsultarListaMonedas,name="ConsultarListaMonedas"),
    path('EditarMoneda/', views.EditarMoneda,name="EditarMoneda"),
    path('HabilitarDeshabilitarMoneda/', views.HabilitarDeshabilitarMoneda,name="HabilitarDeshabilitarMoneda"),
    path('ConsultarListaTransacciones/', views.ConsultarListaTransacciones,name="ConsultarListaTransacciones"),
    path('AgregarMonedaPlataforma/', views.AgregarMonedaPlataforma,name="AgregarMonedaPlataforma"),
    path('AdminEditarMoneda/', views.AdminEditarMoneda,name="AdminEditarMoneda"),

    # Vistas Cliente
    path('InicioCliente/', views.InicioCliente,name="InicioCliente"),
    path('ClienteTransaccion/', views.ClienteTransaccion,name="ClienteTransaccion"),
    path('AgregarDestinatario/', views.AgregarDestinatario,name="AgregarDestinatario"),
    path('ClienteTransaccion/', views.ClienteTransaccion,name="clienteTransaccion"),
    path('EnviarDinero/', views.EnviarDinero,name="EnviarDinero"),
    path('EliminarDestinatario/', views.EliminarDestinatario,name="EliminarDestinatario"),
    path('RecuperarContrasena/', views.RecuperarContrasena,name="RecuperarContrasena"),
    path('EnviarDinero/', views.EnviarDinero,name="EnviarDinero"),
    path('AgregarDinero/', views.AgregarDinero,name="AgregarDinero"),
    #path('ConsultarSaldo/', views.ConsultarSaldo,name="ConsultarSaldo"),
]

