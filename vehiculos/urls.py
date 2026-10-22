from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vehiculos import views

enrutador = routers.DefaultRouter()

enrutador.register(r'perfiles', views.PerfilViewSet)
enrutador.register(r'administradores', views.AdministradorViewSet)
enrutador.register(r'supervisores', views.SupervisorViewSet)
enrutador.register(r'clientes', views.ClienteViewSet)
enrutador.register(r'vehiculos', views.VehiculosViewSet)
enrutador.register(r'estados', views.EstadoViewSet)
enrutador.register(r'gestiones', views.GestionViewSet)
enrutador.register(r'operaciones', views.OperacionViewSet)
enrutador.register(r'datos', views.DatosViewSet)
enrutador.register(r'antecedentes', views.AntecedentesViewSet)
enrutador.register(r'excepcionales', views.ExcepcionalesViewSet)
enrutador.register(r'reglas', views.ReglasViewSet)
enrutador.register(r'consultas', views.ConsultasViewSet)
enrutador.register(r'reportes', views.ReportesViewSet)
enrutador.register(r'indicadores', views.IndicadorViewSet)
enrutador.register(r'tendencias', views.TendenciasViewSet)
enrutador.register(r'actividades', views.ActividadViewSet)
enrutador.register(r'publicas', views.PublicaViewSet)
enrutador.register(r'privadas', views.PrivadaViewSet)

urlpatterns = [
    path('api/', include(enrutador.urls)),  # Prefijo centralizado para todos los ViewSets
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
]