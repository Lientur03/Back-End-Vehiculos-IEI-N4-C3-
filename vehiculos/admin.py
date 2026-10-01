from django.contrib import admin

from .models import Perfil
from .models import Actor
from .models import Estado
from .models import Gestion
from .models import Operacion
from .models import Datos
from .models import Antecedentes
from .models import Excepcionales
from .models import Reglas
from .models import Consultas
from .models import Reportes
from .models import Indicador
from .models import Tendencias
from .models import Actividad
from .models import Publica
from .models import Privada

# Register your models here.
admin.site.register(Perfil)
admin.site.registrer(Actor)
admin.site.register(Estado)
admin.site.registrer(Gestion)
admin.site.register(Operacion)
admin.site.registrer(Datos)
admin.site.register(Antecedentes)
admin.site.registrer(Excepcionales)
admin.site.register(Reglas)
admin.site.registrer(Consultas)
admin.site.register(Reportes)
admin.site.registrer(Indicador)
admin.site.register(Tendencias)
admin.site.registrer(Actividad)
admin.site.register(Publica)
admin.site.registrer(Privada)