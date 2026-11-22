from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets

from . import models as mod
from . import serializer as ser
from . import forms as fo

def index(request):
    return render(request, 'index.html')

# ==========================================
# API RESTful ViewSets, ListView, CreateView, UpdateView, DetailView y DeleteView (Unidad 3)
# ==========================================

# ==========================================
# Clase base para cambio de estado booleano vía POST / fetch
# ==========================================
class BaseCambiarEstadoView(UpdateView):
    fields = []

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(*args, **kwargs)
        for field_name, value in request.POST.items():
            if field_name in ("csrfmiddlewaretoken",):
                continue
            if hasattr(self.object, field_name):
                field = self.object._meta.get_field(field_name)
                if field.get_internal_type() == "BooleanField":
                    setattr(self.object, field_name, str(value).lower() in ("true", "1", "on"))
        self.object.save()
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"ok": True})
        return redirect(request.META.get("HTTP_REFERER", "/"))


# === Vista de registro y manejo de sesión === #
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro Exitoso. ¡Bienvenido!")
            return redirect('/')
        else:
            messages.error(request, "No ha sido posible Registrarlo. Por favor revise el formulario.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

# === Vista Pública de Bienvenida === #
def index(request):
    contexto = {}
    if request.user.is_authenticated:
        if 'mensaje_bienvenida' not in request.session:
            request.session['mensaje_bienvenida'] = f"¡Bienvenido, {request.user.username}!"
        contexto['mensaje_bienvenida'] = request.session.get('mensaje_bienvenida')

    return render(request, 'index.html', contexto)

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
    success_url = reverse_lazy('listar_actividades')
    template_name = 'vehiculos/Actividad/crear_actividad.html'

class ActividadUpdateView(UpdateView):
    model = mod.Actividad
    form_class = fo.ActividadForm
    template_name = 'vehiculos/Actividad/editar_actividad.html'
    success_url = reverse_lazy('listar_actividades')

class ActividadDetailView(DetailView):
    model = mod.Actividad
    template_name = 'vehiculos/Actividad/detalle_actividad.html'

class CambiarActividadHabilitadoView(BaseCambiarEstadoView):
    model = mod.Actividad

class ActividadDeleteView(DeleteView):
    model = mod.Actividad
    template_name = 'vehiculos/Actividad/eliminar_actividad.html'
    success_url = reverse_lazy('listar_actividades')

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
    success_url = reverse_lazy('listar_administradores')
    template_name = 'vehiculos/Administrador/crear_administrador.html'

class AdministradorUpdateView(UpdateView):
    model = mod.Administrador
    form_class = fo.AdministradorForm
    template_name = 'vehiculos/Administrador/editar_administrador.html'
    success_url = reverse_lazy('listar_administradores')

class AdministradorDetailView(DetailView):
    model = mod.Administrador
    template_name = 'vehiculos/Administrador/detalle_administrador.html'

class CambiarAdministradorHabilitadoView(BaseCambiarEstadoView):
    model = mod.Administrador

class AdministradorDeleteView(DeleteView):
    model = mod.Administrador
    template_name = 'vehiculos/Administrador/eliminar_administrador.html'
    success_url = reverse_lazy('listar_administradores')

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
    success_url = reverse_lazy('listar_antecedentes')
    template_name = 'vehiculos/Antecedentes/crear_antecedente.html'

class AntecedentesUpdateView(UpdateView):
    model = mod.Antecedentes
    form_class = fo.AntecedentesForm
    template_name = 'vehiculos/Antecedentes/editar_antecedente.html'
    success_url = reverse_lazy('listar_antecedentes')

class AntecedentesDetailView(DetailView):
    model = mod.Antecedentes
    template_name = 'vehiculos/Antecedentes/detalle_antecedente.html'

class CambiarAntecedentesHabilitadoView(BaseCambiarEstadoView):
    model = mod.Antecedentes

class AntecedentesDeleteView(DeleteView):
    model = mod.Antecedentes
    template_name = 'vehiculos/Antecedentes/eliminar_antecedente.html'
    success_url = reverse_lazy('listar_antecedentes')

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
    success_url = reverse_lazy('listar_clientes')
    template_name = 'vehiculos/Cliente/crear_cliente.html'

class ClienteUpdateView(UpdateView):
    model = mod.Cliente
    form_class = fo.ClienteForm
    template_name = 'vehiculos/Cliente/editar_cliente.html'
    success_url = reverse_lazy('listar_clientes')

class ClienteDetailView(DetailView):
    model = mod.Cliente
    template_name = 'vehiculos/Cliente/detalle_cliente.html'

class CambiarClienteHabilitadoView(BaseCambiarEstadoView):
    model = mod.Cliente

class ClienteDeleteView(DeleteView):
    model = mod.Cliente
    template_name = 'vehiculos/Cliente/eliminar_cliente.html'
    success_url = reverse_lazy('listar_clientes')

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
    success_url = reverse_lazy('listar_consultas')
    template_name = 'vehiculos/Consultas/crear_consulta.html'

class ConsultasUpdateView(UpdateView):
    model = mod.Consultas
    form_class = fo.ConsultasForm
    template_name = 'vehiculos/Consultas/editar_consulta.html'
    success_url = reverse_lazy('listar_consultas')

class ConsultasDetailView(DetailView):
    model = mod.Consultas
    template_name = 'vehiculos/Consultas/detalle_consulta.html'

class CambiarConsultasHabilitadoView(BaseCambiarEstadoView):
    model = mod.Consultas

class ConsultasDeleteView(DeleteView):
    model = mod.Consultas
    template_name = 'vehiculos/Consultas/eliminar_consulta.html'
    success_url = reverse_lazy('listar_consultas')

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
    success_url = reverse_lazy('listar_datos')
    template_name = 'vehiculos/Datos/crear_dato.html'

class DatosUpdateView(UpdateView):
    model = mod.Datos
    form_class = fo.DatosForm
    template_name = 'vehiculos/Datos/editar_dato.html'
    success_url = reverse_lazy('listar_datos')

class DatosDetailView(DetailView):
    model = mod.Datos
    template_name = 'vehiculos/Datos/detalle_dato.html'

class CambiarDatosHabilitadoView(BaseCambiarEstadoView):
    model = mod.Datos

class DatosDeleteView(DeleteView):
    model = mod.Datos
    template_name = 'vehiculos/Datos/eliminar_dato.html'
    success_url = reverse_lazy('listar_datos')

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
    success_url = reverse_lazy('listar_estados')
    template_name = 'vehiculos/Estado/crear_estado.html'

class EstadoUpdateView(UpdateView):
    model = mod.Estado
    form_class = fo.EstadoForm
    template_name = 'vehiculos/Estado/editar_estado.html'
    success_url = reverse_lazy('listar_estados')

class EstadoDetailView(DetailView):
    model = mod.Estado
    template_name = 'vehiculos/Estado/detalle_estado.html'

class CambiarEstadoHabilitadoView(BaseCambiarEstadoView):
    model = mod.Estado

class EstadoDeleteView(DeleteView):
    model = mod.Estado
    template_name = 'vehiculos/Estado/eliminar_estado.html'
    success_url = reverse_lazy('listar_estados')

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
    success_url = reverse_lazy('listar_excepcionales')
    template_name = 'vehiculos/Excepcionales/crear_excepcional.html'

class ExcepcionalesUpdateView(UpdateView):
    model = mod.Excepcionales
    form_class = fo.ExcepcionalesForm
    template_name = 'vehiculos/Excepcionales/editar_excepcional.html'
    success_url = reverse_lazy('listar_excepcionales')

class ExcepcionalesDetailView(DetailView):
    model = mod.Excepcionales
    template_name = 'vehiculos/Excepcionales/detalle_excepcional.html'

class CambiarExcepcionalesHabilitadoView(BaseCambiarEstadoView):
    model = mod.Excepcionales

class ExcepcionalesDeleteView(DeleteView):
    model = mod.Excepcionales
    template_name = 'vehiculos/Excepcionales/eliminar_excepcional.html'
    success_url = reverse_lazy('listar_excepcionales')

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
    success_url = reverse_lazy('listar_gestiones')
    template_name = 'vehiculos/Gestion/crear_gestion.html'

class GestionUpdateView(UpdateView):
    model = mod.Gestion
    form_class = fo.GestionForm
    template_name = 'vehiculos/Gestion/editar_gestion.html'
    success_url = reverse_lazy('listar_gestiones')

class GestionDetailView(DetailView):
    model = mod.Gestion
    template_name = 'vehiculos/Gestion/detalle_gestion.html'

class CambiarGestionHabilitadoView(BaseCambiarEstadoView):
    model = mod.Gestion

class GestionDeleteView(DeleteView):
    model = mod.Gestion
    template_name = 'vehiculos/Gestion/eliminar_gestion.html'
    success_url = reverse_lazy('listar_gestiones')

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
    success_url = reverse_lazy('listar_indicadores')
    template_name = 'vehiculos/Indicador/crear_indicador.html'

class IndicadorUpdateView(UpdateView):
    model = mod.Indicador
    form_class = fo.IndicadorForm
    template_name = 'vehiculos/Indicador/editar_indicador.html'
    success_url = reverse_lazy('listar_indicadores')

class IndicadorDetailView(DetailView):
    model = mod.Indicador
    template_name = 'vehiculos/Indicador/detalle_indicador.html'

class CambiarIndicadorHabilitadoView(BaseCambiarEstadoView):
    model = mod.Indicador

class IndicadorDeleteView(DeleteView):
    model = mod.Indicador
    template_name = 'vehiculos/Indicador/eliminar_indicador.html'
    success_url = reverse_lazy('listar_indicadores')

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
    success_url = reverse_lazy('listar_operaciones')
    template_name = 'vehiculos/Operacion/crear_operacion.html'

class OperacionUpdateView(UpdateView):
    model = mod.Operacion
    form_class = fo.OperacionForm
    template_name = 'vehiculos/Operacion/editar_operacion.html'
    success_url = reverse_lazy('listar_operaciones')

class OperacionDetailView(DetailView):
    model = mod.Operacion
    template_name = 'vehiculos/Operacion/detalle_operacion.html'

class CambiarOperacionHabilitadoView(BaseCambiarEstadoView):
    model = mod.Operacion

class OperacionDeleteView(DeleteView):
    model = mod.Operacion
    template_name = 'vehiculos/Operacion/eliminar_operacion.html'
    success_url = reverse_lazy('listar_operaciones')

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
    success_url = reverse_lazy('listar_perfiles')
    template_name = 'vehiculos/Perfil/crear_perfil.html'

class PerfilUpdateView(UpdateView):
    model = mod.Perfil
    form_class = fo.PerfilForm
    template_name = 'vehiculos/Perfil/editar_perfil.html'
    success_url = reverse_lazy('listar_perfiles')

class PerfilDetailView(DetailView):
    model = mod.Perfil
    template_name = 'vehiculos/Perfil/detalle_perfil.html'

class CambiarPerfilHabilitadoView(BaseCambiarEstadoView):
    model = mod.Perfil

class PerfilDeleteView(DeleteView):
    model = mod.Perfil
    template_name = 'vehiculos/Perfil/eliminar_perfil.html'
    success_url = reverse_lazy('listar_perfiles')

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
    success_url = reverse_lazy('listar_privadas')
    template_name = 'vehiculos/Privada/crear_privada.html'

class PrivadaUpdateView(UpdateView):
    model = mod.Privada
    form_class = fo.PrivadaForm
    template_name = 'vehiculos/Privada/editar_privada.html'
    success_url = reverse_lazy('listar_privadas')

class PrivadaDetailView(DetailView):
    model = mod.Privada
    template_name = 'vehiculos/Privada/detalle_privada.html'

class CambiarPrivadaHabilitadoView(BaseCambiarEstadoView):
    model = mod.Privada

class PrivadaDeleteView(DeleteView):
    model = mod.Privada
    template_name = 'vehiculos/Privada/eliminar_privada.html'
    success_url = reverse_lazy('listar_privadas')

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
    success_url = reverse_lazy('listar_publicas')
    template_name = 'vehiculos/Publica/crear_publica.html'

class PublicaUpdateView(UpdateView):
    model = mod.Publica
    form_class = fo.PublicaForm
    template_name = 'vehiculos/Publica/editar_publica.html'
    success_url = reverse_lazy('listar_publicas')

class PublicaDetailView(DetailView):
    model = mod.Publica
    template_name = 'vehiculos/Publica/detalle_publica.html'

class CambiarPublicaHabilitadoView(BaseCambiarEstadoView):
    model = mod.Publica

class PublicaDeleteView(DeleteView):
    model = mod.Publica
    template_name = 'vehiculos/Publica/eliminar_publica.html'
    success_url = reverse_lazy('listar_publicas')

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
    success_url = reverse_lazy('listar_reglas')
    template_name = 'vehiculos/Reglas/crear_reglas.html'

class ReglasUpdateView(UpdateView):
    model = mod.Reglas
    form_class = fo.ReglasForm
    template_name = 'vehiculos/Reglas/editar_reglas.html'
    success_url = reverse_lazy('listar_reglas')

class ReglasDetailView(DetailView):
    model = mod.Reglas
    template_name = 'vehiculos/Reglas/detalle_reglas.html'

class CambiarReglasHabilitadoView(BaseCambiarEstadoView):
    model = mod.Reglas

class ReglasDeleteView(DeleteView):
    model = mod.Reglas
    template_name = 'vehiculos/Reglas/eliminar_regla.html'
    success_url = reverse_lazy('listar_reglas')

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
    success_url = reverse_lazy('listar_reportes')
    template_name = 'vehiculos/Reportes/crear_reporte.html'

class ReportesUpdateView(UpdateView):
    model = mod.Reportes
    form_class = fo.ReportesForm
    template_name = 'vehiculos/Reportes/editar_reporte.html'
    success_url = reverse_lazy('listar_reportes')

class ReportesDetailView(DetailView):
    model = mod.Reportes
    template_name = 'vehiculos/Reportes/detalle_reporte.html'

class CambiarReportesHabilitadoView(BaseCambiarEstadoView):
    model = mod.Reportes

class ReportesDeleteView(DeleteView):
    model = mod.Reportes
    template_name = 'vehiculos/Reportes/eliminar_reporte.html'
    success_url = reverse_lazy('listar_reportes')

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
    success_url = reverse_lazy('listar_supervisores')
    template_name = 'vehiculos/Supervisor/crear_supervisor.html'

class SupervisorUpdateView(UpdateView):
    model = mod.Supervisor
    form_class = fo.SupervisorForm
    template_name = 'vehiculos/Supervisor/editar_supervisor.html'
    success_url = reverse_lazy('listar_supervisores')

class SupervisorDetailView(DetailView):
    model = mod.Supervisor
    template_name = 'vehiculos/Supervisor/detalle_supervisor.html'

class CambiarSupervisorHabilitadoView(BaseCambiarEstadoView):
    model = mod.Supervisor

class SupervisorDeleteView(DeleteView):
    model = mod.Supervisor
    template_name = 'vehiculos/Supervisor/eliminar_supervisor.html'
    success_url = reverse_lazy('listar_supervisores')

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
    success_url = reverse_lazy('listar_tendencias')
    template_name = 'vehiculos/Tendencias/crear_tendencia.html'

class TendenciasUpdateView(UpdateView):
    model = mod.Tendencias
    form_class = fo.TendenciasForm
    template_name = 'vehiculos/Tendencias/editar_tendencia.html'
    success_url = reverse_lazy('listar_tendencias')

class TendenciasDetailView(DetailView):
    model = mod.Tendencias
    template_name = 'vehiculos/Tendencias/detalle_tendencia.html'

class CambiarTendenciasHabilitadoView(BaseCambiarEstadoView):
    model = mod.Tendencias

class TendenciasDeleteView(DeleteView):
    model = mod.Tendencias
    template_name = 'vehiculos/Tendencias/eliminar_tendencia.html'
    success_url = reverse_lazy('listar_tendencias')

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
    success_url = reverse_lazy('listar_vehiculos')
    template_name = 'vehiculos/Vehiculos/crear_vehiculo.html'

class VehiculosUpdateView(UpdateView):
    model = mod.Vehiculos
    form_class = fo.VehiculosForm
    template_name = 'vehiculos/Vehiculos/editar_vehiculo.html'
    success_url = reverse_lazy('listar_vehiculos')

class VehiculosDetailView(DetailView):
    model = mod.Vehiculos
    template_name = 'vehiculos/Vehiculos/detalle_vehiculo.html'

class CambiarVehiculosHabilitadoView(BaseCambiarEstadoView):
    model = mod.Vehiculos

class VehiculosDeleteView(DeleteView):
    model = mod.Vehiculos
    template_name = 'vehiculos/Vehiculos/eliminar_vehiculo.html'
    success_url = reverse_lazy('listar_vehiculos')