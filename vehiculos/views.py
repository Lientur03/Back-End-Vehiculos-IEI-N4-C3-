from django.shortcuts import render
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from . import models as mod
from . import serializer as ser
from . import forms as fo

def index(request):
    return render(request, 'index.html')

# ==========================================
# API RESTful ViewSets, ListView, CreateView (Unidad 3)
# ==========================================

# ============
# 1. ACTIVIDAD
# ============
class ActividadViewSet(viewsets.ModelViewSet):
    queryset = mod.Actividad.objects.all()
    serializer_class = ser.ActividadSerializer

class ActividadListView(ListView):
    model = mod.Actividad
    template_name = 'vehiculos/Actividad/listar_actividades.html'
    context_object_name = 'actividades'

class ActividadCreateView(CreateView):
    form_class = fo.ActividadForm
    model = mod.Actividad
    success_url = 'listar_actividades'
    template_name = 'vehiculos/Actividad/crear_actividad.html'

# ================
# 2. ADMINISTRADOR
# ================
class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = mod.Administrador.objects.all()
    serializer_class = ser.AdministradorSerializer

class AdministradorListView(ListView):
    model = mod.Administrador
    template_name = 'vehiculos/Administrador/listar_administradores.html'
    context_object_name = 'administradores'

class AdministradorCreateView(CreateView):
    form_class = fo.AdministradorForm
    model = mod.Administrador
    success_url = 'listar_administradores'
    template_name = 'vehiculos/Administrador/crear_administrador.html'

# ===============
# 3. ANTECEDENTES
# ===============
class AntecedentesViewSet(viewsets.ModelViewSet):
    queryset = mod.Antecedentes.objects.all()
    serializer_class = ser.AntecedentesSerializer

class AntecedentesListView(ListView):
    model = mod.Antecedentes
    template_name = 'vehiculos/Antecedentes/listar_antecedentes.html'
    context_object_name = 'antecedentes'

class AntecedentesCreateView(CreateView):
    form_class = fo.AntecedentesForm
    model = mod.Antecedentes
    success_url = 'listar_antecedentes'
    template_name = 'vehiculos/Antecedentes/crear_antecedente.html'

# ==========
# 4. CLIENTE
# ==========
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = mod.Cliente.objects.all()
    serializer_class = ser.ClienteSerializer

class ClienteListView(ListView):
    model = mod.Cliente
    template_name = 'vehiculos/Cliente/listar_clientes.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    form_class = fo.ClienteForm
    model = mod.Cliente
    success_url = 'listar_clientes'
    template_name = 'vehiculos/Cliente/crear_cliente.html'

# ============
# 5. CONSULTAS
# ============
class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = mod.Consultas.objects.all()
    serializer_class = ser.ConsultasSerializer

class ConsultasListView(ListView):
    model = mod.Consultas
    template_name = 'vehiculos/Consultas/listar_consultas.html'
    context_object_name = 'consultas'

class ConsultasCreateView(CreateView):
    form_class = fo.ConsultasForm
    model = mod.Consultas
    success_url = 'listar_consultas'
    template_name = 'vehiculos/Consultas/crear_consulta.html'

# ========
# 6. DATOS
# ========
class DatosViewSet(viewsets.ModelViewSet):
    queryset = mod.Datos.objects.all()
    serializer_class = ser.DatosSerializer

class DatosListView(ListView):
    model = mod.Datos
    template_name = 'vehiculos/Datos/listar_datos.html'
    context_object_name = 'datos'

class DatosCreateView(CreateView):
    form_class = fo.DatosForm
    model = mod.Datos
    success_url = 'listar_datos'
    template_name = 'vehiculos/Datos/crear_dato.html'

# =========
# 7. ESTADO
# =========
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = mod.Estado.objects.all()
    serializer_class = ser.EstadoSerializer

class EstadoListView(ListView):
    model = mod.Estado
    template_name = 'vehiculos/Estado/listar_estados.html'
    context_object_name = 'estados'

class EstadoCreateView(CreateView):
    form_class = fo.EstadoForm
    model = mod.Estado
    success_url = 'listar_estados'
    template_name = 'vehiculos/Estado/crear_estado.html'

# ================
# 8. EXCEPCIONALES
# ================
class ExcepcionalesViewSet(viewsets.ModelViewSet):
    queryset = mod.Excepcionales.objects.all()
    serializer_class = ser.ExcepcionalesSerializer

class ExcepcionalesListView(ListView):
    model = mod.Excepcionales
    template_name = 'vehiculos/Excepcionales/listar_excepcionales.html'
    context_object_name = 'excepcionales'

class ExcepcionalesCreateView(CreateView):
    form_class = fo.ExcepcionalesForm
    model = mod.Excepcionales
    success_url = 'listar_excepcionales'
    template_name = 'vehiculos/Excepcionales/crear_excepcional.html'

# ==========
# 9. GESTION
# ==========
class GestionViewSet(viewsets.ModelViewSet):
    queryset = mod.Gestion.objects.all()
    serializer_class = ser.GestionSerializer

class GestionListView(ListView):
    model = mod.Gestion
    template_name = 'vehiculos/Gestion/listar_gestiones.html'
    context_object_name = 'gestiones'

class GestionCreateView(CreateView):
    form_class = fo.GestionForm
    model = mod.Gestion
    success_url = 'listar_gestiones'
    template_name = 'vehiculos/Gestion/crear_gestion.html'

# =============
# 10. INDICADOR
# =============
class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = mod.Indicador.objects.all()
    serializer_class = ser.IndicadorSerializer

class IndicadorListView(ListView):
    model = mod.Indicador
    template_name = 'vehiculos/Indicador/listar_indicadores.html'
    context_object_name = 'indicadores'

class IndicadorCreateView(CreateView):
    form_class = fo.IndicadorForm
    model = mod.Indicador
    success_url = 'listar_indicadores'
    template_name = 'vehiculos/Indicador/crear_indicador.html'

# =============
# 11. OPERACION
# =============
class OperacionViewSet(viewsets.ModelViewSet):
    queryset = mod.Operacion.objects.all()
    serializer_class = ser.OperacionSerializer

class OperacionListView(ListView):
    model = mod.Operacion
    template_name = 'vehiculos/Operacion/listar_operaciones.html'
    context_object_name = 'operaciones'

class OperacionCreateView(CreateView):
    form_class = fo.OperacionForm
    model = mod.Operacion
    success_url = 'listar_operaciones'
    template_name = 'vehiculos/Operacion/crear_operacion.html'

# ==========
# 12. PERFIL
# ==========
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = mod.Perfil.objects.all()
    serializer_class = ser.PerfilSerializer

class PerfilListView(ListView):
    model = mod.Perfil
    template_name = 'vehiculos/Perfil/listar_perfiles.html'
    context_object_name = 'perfiles'

class PerfilCreateView(CreateView):
    form_class = fo.PerfilForm
    model = mod.Perfil
    success_url = 'listar_perfiles'
    template_name = 'vehiculos/Perfil/crear_perfil.html'

# ===========
# 13. PRIVADA
# ===========
class PrivadaViewSet(viewsets.ModelViewSet):
    queryset = mod.Privada.objects.all()
    serializer_class = ser.PrivadaSerializer

class PrivadaListView(ListView):
    model = mod.Privada
    template_name = 'vehiculos/Privada/listar_privadas.html'
    context_object_name = 'privadas'

class PrivadaCreateView(CreateView):
    form_class = fo.PrivadaForm
    model = mod.Privada
    success_url = 'listar_privadas'
    template_name = 'vehiculos/Privada/crear_privada.html'

# ===========
# 14. PUBLICA
# ===========
class PublicaViewSet(viewsets.ModelViewSet):
    queryset = mod.Publica.objects.all()
    serializer_class = ser.PublicaSerializer

class PublicaListView(ListView):
    model = mod.Publica
    template_name = 'vehiculos/Publica/listar_publicas.html'
    context_object_name = 'publicas'

class PublicaCreateView(CreateView):
    form_class = fo.PublicaForm
    model = mod.Publica
    success_url = 'listar_publicas'
    template_name = 'vehiculos/Publica/crear_publica.html'

# ==========
# 15. REGLAS
# ==========
class ReglasViewSet(viewsets.ModelViewSet):
    queryset = mod.Reglas.objects.all()
    serializer_class = ser.ReglasSerializer

class ReglasListView(ListView):
    model = mod.Reglas
    template_name = 'vehiculos/Reglas/listar_reglas.html'
    context_object_name = 'reglas'

class ReglasCreateView(CreateView):
    form_class = fo.ReglasForm
    model = mod.Reglas
    success_url = 'listar_reglas'
    template_name = 'vehiculos/Reglas/crear_reglas.html'

# ============
# 16. REPORTES
# ============
class ReportesViewSet(viewsets.ModelViewSet):
    queryset = mod.Reportes.objects.all()
    serializer_class = ser.ReportesSerializer

class ReportesListView(ListView):
    model = mod.Reportes
    template_name = 'vehiculos/Reportes/listar_reportes.html'
    context_object_name = 'reportes'

class ReportesCreateView(CreateView):
    form_class = fo.ReportesForm
    model = mod.Reportes
    success_url = 'listar_reportes'
    template_name = 'vehiculos/Reportes/crear_reporte.html'

# ==============
# 17. SUPERVISOR
# ==============
class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = mod.Supervisor.objects.all()
    serializer_class = ser.SupervisorSerializer

class SupervisorListView(ListView):
    model = mod.Supervisor
    template_name = 'vehiculos/Supervisor/listar_supervisores.html'
    context_object_name = 'supervisores'

class SupervisorCreateView(CreateView):
    form_class = fo.SupervisorForm
    model = mod.Supervisor
    success_url = 'listar_supervisores'
    template_name = 'vehiculos/Supervisor/crear_supervisor.html'

# ==============
# 18. TENDENCIAS
# ==============
class TendenciasViewSet(viewsets.ModelViewSet):
    queryset = mod.Tendencias.objects.all()
    serializer_class = ser.TendenciasSerializer

class TendenciasListView(ListView):
    model = mod.Tendencias
    template_name = 'vehiculos/Tendencias/listar_tendencias.html'
    context_object_name = 'tendencias'

class TendenciasCreateView(CreateView):
    form_class = fo.TendenciasForm
    model = mod.Tendencias
    success_url = 'listar_tendencias'
    template_name = 'vehiculos/Tendencias/crear_tendencia.html'

# =============
# 19. VEHICULOS
# =============
class VehiculosViewSet(viewsets.ModelViewSet):
    queryset = mod.Vehiculos.objects.all()
    serializer_class = ser.VehiculosSerializer

class VehiculosListView(ListView):
    model = mod.Vehiculos
    template_name = 'vehiculos/Vehiculos/listar_vehiculos.html'
    context_object_name = 'vehiculos'

class VehiculosCreateView(CreateView):
    form_class = fo.VehiculosForm
    model = mod.Vehiculos
    success_url = 'listar_vehiculos'
    template_name = 'vehiculos/Vehiculos/crear_vehiculo.html'