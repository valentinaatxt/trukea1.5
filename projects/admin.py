from django.contrib import admin

from projects.views import monedas as monedas_view

from .models import Destinatarios, Proyecto, Usuario_registrado, monedas
admin.site.register (Proyecto)
admin.site.register(Usuario_registrado)
admin.site.register(Destinatarios)
admin.site.register(monedas)
