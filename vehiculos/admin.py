from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Usuario, Perfil, Administrador, Supervisor, Cliente, Vehiculos, Estado,
    Gestion, Operacion, Datos, Antecedentes, Excepcionales, Reglas,
    Consultas, Reportes, Indicador, Tendencias, Actividad, Publica, Privada
)

# Registramos el usuario personalizado con UserAdmin y todos los modelos en el panel de administración
admin.site.register(Usuario, UserAdmin)
admin.site.register(Perfil)
admin.site.register(Administrador)
admin.site.register(Supervisor)
admin.site.register(Cliente)
admin.site.register(Vehiculos)
admin.site.register(Estado)
admin.site.register(Gestion)
admin.site.register(Operacion)
admin.site.register(Datos)
admin.site.register(Antecedentes)
admin.site.register(Excepcionales)
admin.site.register(Reglas)
admin.site.register(Consultas)
admin.site.register(Reportes)
admin.site.register(Indicador)
admin.site.register(Tendencias)
admin.site.register(Actividad)
admin.site.register(Publica)
admin.site.register(Privada)