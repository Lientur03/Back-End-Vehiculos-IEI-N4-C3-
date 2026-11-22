from django.urls import path, include
from rest_framework import routers
from vehiculos import views

enrutador = routers.DefaultRouter()

# --- API RESTful (19 ViewSets) ---
enrutador.register(r'actividades', views.ActividadViewSet)
enrutador.register(r'administradores', views.AdministradorViewSet)
enrutador.register(r'antecedentes', views.AntecedentesViewSet)
enrutador.register(r'clientes', views.ClienteViewSet)
enrutador.register(r'consultas', views.ConsultasViewSet)
enrutador.register(r'datos', views.DatosViewSet)
enrutador.register(r'estados', views.EstadoViewSet)
enrutador.register(r'excepcionales', views.ExcepcionalesViewSet)
enrutador.register(r'gestiones', views.GestionViewSet)
enrutador.register(r'indicadores', views.IndicadorViewSet)
enrutador.register(r'operaciones', views.OperacionViewSet)
enrutador.register(r'perfiles', views.PerfilViewSet)
enrutador.register(r'privadas', views.PrivadaViewSet)
enrutador.register(r'publicas', views.PublicaViewSet)
enrutador.register(r'reglas', views.ReglasViewSet)
enrutador.register(r'reportes', views.ReportesViewSet)
enrutador.register(r'supervisores', views.SupervisorViewSet)
enrutador.register(r'tendencias', views.TendenciasViewSet)
enrutador.register(r'vehiculos', views.VehiculosViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
    path('index/', views.index, name='index'),

    # 1. ACTIVIDAD
    path('actividades/listar/', views.ActividadListView.as_view(), name='listar_actividades'),
    path('actividades/crear/', views.ActividadCreateView.as_view(), name='crear_actividad'),
    path('actividades/<int:pk>/editar/', views.ActividadUpdateView.as_view(), name='editar_actividad'),
    path('actividades/<int:pk>/detalle/', views.ActividadDetailView.as_view(), name='detalle_actividad'),
    path('actividades/<int:pk>/cambiar-estado/', views.CambiarActividadHabilitadoView.as_view(), name='cambiar_actividad_habilitado'),
    path('actividades/<int:pk>/eliminar/', views.ActividadDeleteView.as_view(), name='eliminar_actividad'),

    # 2. ADMINISTRADOR
    path('administradores/listar/', views.AdministradorListView.as_view(), name='listar_administradores'),
    path('administradores/crear/', views.AdministradorCreateView.as_view(), name='crear_administrador'),
    path('administradores/<int:pk>/editar/', views.AdministradorUpdateView.as_view(), name='editar_administrador'),
    path('administradores/<int:pk>/detalle/', views.AdministradorDetailView.as_view(), name='detalle_administrador'),
    path('administradores/<int:pk>/cambiar-estado/', views.CambiarAdministradorHabilitadoView.as_view(), name='cambiar_administrador_habilitado'),
    path('administradores/<int:pk>/eliminar/', views.AdministradorDeleteView.as_view(), name='eliminar_administrador'),

    # 3. ANTECEDENTES
    path('antecedentes/listar/', views.AntecedentesListView.as_view(), name='listar_antecedentes'),
    path('antecedentes/crear/', views.AntecedentesCreateView.as_view(), name='crear_antecedente'),
    path('antecedentes/<int:pk>/editar/', views.AntecedentesUpdateView.as_view(), name='editar_antecedente'),
    path('antecedentes/<int:pk>/detalle/', views.AntecedentesDetailView.as_view(), name='detalle_antecedente'),
    path('antecedentes/<int:pk>/cambiar-estado/', views.CambiarAntecedentesHabilitadoView.as_view(), name='cambiar_antecedentes_habilitado'),
    path('antecedentes/<int:pk>/eliminar/', views.AntecedentesDeleteView.as_view(), name='eliminar_antecedente'),

    # 4. CLIENTE (PK: rut -> CharField)
    path('clientes/listar/', views.ClienteListView.as_view(), name='listar_clientes'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='crear_cliente'),
    path('clientes/<str:pk>/editar/', views.ClienteUpdateView.as_view(), name='editar_cliente'),
    path('clientes/<str:pk>/detalle/', views.ClienteDetailView.as_view(), name='detalle_cliente'),
    path('clientes/<str:pk>/cambiar-estado/', views.CambiarClienteHabilitadoView.as_view(), name='cambiar_cliente_habilitado'),
    path('clientes/<str:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='eliminar_cliente'),

    # 5. CONSULTAS
    path('consultas/listar/', views.ConsultasListView.as_view(), name='listar_consultas'),
    path('consultas/crear/', views.ConsultasCreateView.as_view(), name='crear_consulta'),
    path('consultas/<int:pk>/editar/', views.ConsultasUpdateView.as_view(), name='editar_consulta'),
    path('consultas/<int:pk>/detalle/', views.ConsultasDetailView.as_view(), name='detalle_consulta'),
    path('consultas/<int:pk>/cambiar-estado/', views.CambiarConsultasHabilitadoView.as_view(), name='cambiar_consultas_habilitado'),
    path('consultas/<int:pk>/eliminar/', views.ConsultasDeleteView.as_view(), name='eliminar_consulta'),

    # 6. DATOS
    path('datos/listar/', views.DatosListView.as_view(), name='listar_datos'),
    path('datos/crear/', views.DatosCreateView.as_view(), name='crear_dato'),
    path('datos/<int:pk>/editar/', views.DatosUpdateView.as_view(), name='editar_dato'),
    path('datos/<int:pk>/detalle/', views.DatosDetailView.as_view(), name='detalle_dato'),
    path('datos/<int:pk>/cambiar-estado/', views.CambiarDatosHabilitadoView.as_view(), name='cambiar_datos_habilitado'),
    path('datos/<int:pk>/eliminar/', views.DatosDeleteView.as_view(), name='eliminar_dato'),

    # 7. ESTADO
    path('estados/listar/', views.EstadoListView.as_view(), name='listar_estados'),
    path('estados/crear/', views.EstadoCreateView.as_view(), name='crear_estado'),
    path('estados/<int:pk>/editar/', views.EstadoUpdateView.as_view(), name='editar_estado'),
    path('estados/<int:pk>/detalle/', views.EstadoDetailView.as_view(), name='detalle_estado'),
    path('estados/<int:pk>/cambiar-estado/', views.CambiarEstadoHabilitadoView.as_view(), name='cambiar_estado_habilitado'),
    path('estados/<int:pk>/eliminar/', views.EstadoDeleteView.as_view(), name='eliminar_estado'),

    # 8. EXCEPCIONALES
    path('excepcionales/listar/', views.ExcepcionalesListView.as_view(), name='listar_excepcionales'),
    path('excepcionales/crear/', views.ExcepcionalesCreateView.as_view(), name='crear_excepcional'),
    path('excepcionales/<int:pk>/editar/', views.ExcepcionalesUpdateView.as_view(), name='editar_excepcional'),
    path('excepcionales/<int:pk>/detalle/', views.ExcepcionalesDetailView.as_view(), name='detalle_excepcional'),
    path('excepcionales/<int:pk>/cambiar-estado/', views.CambiarExcepcionalesHabilitadoView.as_view(), name='cambiar_excepcionales_habilitado'),
    path('excepcionales/<int:pk>/eliminar/', views.ExcepcionalesDeleteView.as_view(), name='eliminar_excepcional'),

    # 9. GESTION
    path('gestiones/listar/', views.GestionListView.as_view(), name='listar_gestiones'),
    path('gestiones/crear/', views.GestionCreateView.as_view(), name='crear_gestion'),
    path('gestiones/<int:pk>/editar/', views.GestionUpdateView.as_view(), name='editar_gestion'),
    path('gestiones/<int:pk>/detalle/', views.GestionDetailView.as_view(), name='detalle_gestion'),
    path('gestiones/<int:pk>/cambiar-estado/', views.CambiarGestionHabilitadoView.as_view(), name='cambiar_gestion_habilitado'),
    path('gestiones/<int:pk>/eliminar/', views.GestionDeleteView.as_view(), name='eliminar_gestion'),

    # 10. INDICADOR
    path('indicadores/listar/', views.IndicadorListView.as_view(), name='listar_indicadores'),
    path('indicadores/crear/', views.IndicadorCreateView.as_view(), name='crear_indicador'),
    path('indicadores/<int:pk>/editar/', views.IndicadorUpdateView.as_view(), name='editar_indicador'),
    path('indicadores/<int:pk>/detalle/', views.IndicadorDetailView.as_view(), name='detalle_indicador'),
    path('indicadores/<int:pk>/cambiar-estado/', views.CambiarIndicadorHabilitadoView.as_view(), name='cambiar_indicador_habilitado'),
    path('indicadores/<int:pk>/eliminar/', views.IndicadorDeleteView.as_view(), name='eliminar_indicador'),

    # 11. OPERACION
    path('operaciones/listar/', views.OperacionListView.as_view(), name='listar_operaciones'),
    path('operaciones/crear/', views.OperacionCreateView.as_view(), name='crear_operacion'),
    path('operaciones/<int:pk>/editar/', views.OperacionUpdateView.as_view(), name='editar_operacion'),
    path('operaciones/<int:pk>/detalle/', views.OperacionDetailView.as_view(), name='detalle_operacion'),
    path('operaciones/<int:pk>/cambiar-estado/', views.CambiarOperacionHabilitadoView.as_view(), name='cambiar_operacion_habilitado'),
    path('operaciones/<int:pk>/eliminar/', views.OperacionDeleteView.as_view(), name='eliminar_operacion'),

    # 12. PERFIL
    path('perfiles/listar/', views.PerfilListView.as_view(), name='listar_perfiles'),
    path('perfiles/crear/', views.PerfilCreateView.as_view(), name='crear_perfil'),
    path('perfiles/<int:pk>/editar/', views.PerfilUpdateView.as_view(), name='editar_perfil'),
    path('perfiles/<int:pk>/detalle/', views.PerfilDetailView.as_view(), name='detalle_perfil'),
    path('perfiles/<int:pk>/cambiar-estado/', views.CambiarPerfilHabilitadoView.as_view(), name='cambiar_perfil_habilitado'),
    path('perfiles/<int:pk>/eliminar/', views.PerfilDeleteView.as_view(), name='eliminar_perfil'),

    # 13. PRIVADA
    path('privadas/listar/', views.PrivadaListView.as_view(), name='listar_privadas'),
    path('privadas/crear/', views.PrivadaCreateView.as_view(), name='crear_privada'),
    path('privadas/<int:pk>/editar/', views.PrivadaUpdateView.as_view(), name='editar_privada'),
    path('privadas/<int:pk>/detalle/', views.PrivadaDetailView.as_view(), name='detalle_privada'),
    path('privadas/<int:pk>/cambiar-estado/', views.CambiarPrivadaHabilitadoView.as_view(), name='cambiar_privada_habilitado'),
    path('privadas/<int:pk>/eliminar/', views.PrivadaDeleteView.as_view(), name='eliminar_privada'),

    # 14. PUBLICA
    path('publicas/listar/', views.PublicaListView.as_view(), name='listar_publicas'),
    path('publicas/crear/', views.PublicaCreateView.as_view(), name='crear_publica'),
    path('publicas/<int:pk>/editar/', views.PublicaUpdateView.as_view(), name='editar_publica'),
    path('publicas/<int:pk>/detalle/', views.PublicaDetailView.as_view(), name='detalle_publica'),
    path('publicas/<int:pk>/cambiar-estado/', views.CambiarPublicaHabilitadoView.as_view(), name='cambiar_publica_habilitado'),
    path('publicas/<int:pk>/eliminar/', views.PublicaDeleteView.as_view(), name='eliminar_publica'),

    # 15. REGLAS
    path('reglas/listar/', views.ReglasListView.as_view(), name='listar_reglas'),
    path('reglas/crear/', views.ReglasCreateView.as_view(), name='crear_reglas'),
    path('reglas/<int:pk>/editar/', views.ReglasUpdateView.as_view(), name='editar_reglas'),
    path('reglas/<int:pk>/detalle/', views.ReglasDetailView.as_view(), name='detalle_reglas'),
    path('reglas/<int:pk>/cambiar-estado/', views.CambiarReglasHabilitadoView.as_view(), name='cambiar_reglas_habilitado'),
    path('reglas/<int:pk>/eliminar/', views.ReglasDeleteView.as_view(), name='eliminar_regla'),

    # 16. REPORTES
    path('reportes/listar/', views.ReportesListView.as_view(), name='listar_reportes'),
    path('reportes/crear/', views.ReportesCreateView.as_view(), name='crear_reporte'),
    path('reportes/<int:pk>/editar/', views.ReportesUpdateView.as_view(), name='editar_reporte'),
    path('reportes/<int:pk>/detalle/', views.ReportesDetailView.as_view(), name='detalle_reporte'),
    path('reportes/<int:pk>/cambiar-estado/', views.CambiarReportesHabilitadoView.as_view(), name='cambiar_reportes_habilitado'),
    path('reportes/<int:pk>/eliminar/', views.ReportesDeleteView.as_view(), name='eliminar_reporte'),

    # 17. SUPERVISOR
    path('supervisores/listar/', views.SupervisorListView.as_view(), name='listar_supervisores'),
    path('supervisores/crear/', views.SupervisorCreateView.as_view(), name='crear_supervisor'),
    path('supervisores/<int:pk>/editar/', views.SupervisorUpdateView.as_view(), name='editar_supervisor'),
    path('supervisores/<int:pk>/detalle/', views.SupervisorDetailView.as_view(), name='detalle_supervisor'),
    path('supervisores/<int:pk>/cambiar-estado/', views.CambiarSupervisorHabilitadoView.as_view(), name='cambiar_supervisor_habilitado'),
    path('supervisores/<int:pk>/eliminar/', views.SupervisorDeleteView.as_view(), name='eliminar_supervisor'),

    # 18. TENDENCIAS
    path('tendencias/listar/', views.TendenciasListView.as_view(), name='listar_tendencias'),
    path('tendencias/crear/', views.TendenciasCreateView.as_view(), name='crear_tendencia'),
    path('tendencias/<int:pk>/editar/', views.TendenciasUpdateView.as_view(), name='editar_tendencia'),
    path('tendencias/<int:pk>/detalle/', views.TendenciasDetailView.as_view(), name='detalle_tendencia'),
    path('tendencias/<int:pk>/cambiar-estado/', views.CambiarTendenciasHabilitadoView.as_view(), name='cambiar_tendencias_habilitado'),
    path('tendencias/<int:pk>/eliminar/', views.TendenciasDeleteView.as_view(), name='eliminar_tendencia'),

    # 19. VEHICULOS (PK: patente -> CharField)
    path('vehiculos/listar/', views.VehiculosListView.as_view(), name='listar_vehiculos'),
    path('vehiculos/crear/', views.VehiculosCreateView.as_view(), name='crear_vehiculo'),
    path('vehiculos/<str:pk>/editar/', views.VehiculosUpdateView.as_view(), name='editar_vehiculo'),
    path('vehiculos/<str:pk>/detalle/', views.VehiculosDetailView.as_view(), name='detalle_vehiculo'),
    path('vehiculos/<str:pk>/cambiar-estado/', views.CambiarVehiculosHabilitadoView.as_view(), name='cambiar_vehiculos_habilitado'),
    path('vehiculos/<str:pk>/eliminar/', views.VehiculosDeleteView.as_view(), name='eliminar_vehiculo'),
]