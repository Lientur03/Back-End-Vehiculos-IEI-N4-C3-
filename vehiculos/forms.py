from django import forms
from .models import (
    Perfil, Administrador, Supervisor, Cliente, Vehiculos,
    Estado, Gestion, Operacion, Datos, Antecedentes,
    Excepcionales, Reglas, Consultas, Reportes, Indicador,
    Tendencias, Actividad, Publica, Privada
)


class BaseBootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                existing_class = widget.attrs.get("class", "")
                widget.attrs["class"] = f"{existing_class} form-check-input".strip()
            elif isinstance(widget, forms.Select):
                existing_class = widget.attrs.get("class", "")
                widget.attrs["class"] = f"{existing_class} form-select".strip()
            else:
                existing_class = widget.attrs.get("class", "")
                widget.attrs["class"] = f"{existing_class} form-control".strip()


class PerfilForm(BaseBootstrapForm):
    class Meta:
        model = Perfil
        fields = ["usuario", "rol", "nivel_acceso", "departamento"]


class AdministradorForm(BaseBootstrapForm):
    class Meta:
        model = Administrador
        fields = ["nombre", "correo"]


class SupervisorForm(BaseBootstrapForm):
    class Meta:
        model = Supervisor
        fields = ["nombre", "correo", "perfil"]


class ClienteForm(BaseBootstrapForm):
    class Meta:
        model = Cliente
        fields = ["rut", "nombre", "correo", "telefono", "direccion"]


class VehiculosForm(BaseBootstrapForm):
    class Meta:
        model = Vehiculos
        fields = ["patente", "marca", "modelo", "anio", "tipo_combustible", "cliente"]


class EstadoForm(BaseBootstrapForm):
    class Meta:
        model = Estado
        fields = ["nombre", "descripcion", "es_activo"]


class GestionForm(BaseBootstrapForm):
    class Meta:
        model = Gestion
        fields = ["codigo_flota", "nombre_area", "responsable", "fecha_inicio", "activo"]
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
        }


class OperacionForm(BaseBootstrapForm):
    class Meta:
        model = Operacion
        fields = [
            "gestion", "actor", "patente_vehiculo", "tipo_operacion",
            "fecha_inicio", "fecha_fin", "observaciones"
        ]
        widgets = {
            "fecha_inicio": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "fecha_fin": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class DatosForm(BaseBootstrapForm):
    class Meta:
        model = Datos
        fields = ["operacion", "kilometraje", "nivel_combustible"]


class AntecedentesForm(BaseBootstrapForm):
    class Meta:
        model = Antecedentes
        fields = ["vehiculo", "fecha_evento", "tipo_antecedente", "descripcion", "archivo_adjunto"]
        widgets = {
            "fecha_evento": forms.DateInput(attrs={"type": "date"}),
        }


class ExcepcionalesForm(BaseBootstrapForm):
    class Meta:
        model = Excepcionales
        fields = ["operacion", "titulo", "descripcion", "nivel_prioridad", "resuelto"]


class ReglasForm(BaseBootstrapForm):
    class Meta:
        model = Reglas
        fields = ["nombre_regla", "limite_kilometros_mantencion", "dias_maximo_revision", "activa"]


class ConsultasForm(BaseBootstrapForm):
    class Meta:
        model = Consultas
        fields = ["usuario", "nombre_consulta", "criterios_busqueda"]


class ReportesForm(BaseBootstrapForm):
    class Meta:
        model = Reportes
        fields = ["titulo", "tipo_reporte", "generado_por", "parametros_usados"]


class IndicadorForm(BaseBootstrapForm):
    class Meta:
        model = Indicador
        fields = ["nombre", "valor", "unidad_medida"]


class TendenciasForm(BaseBootstrapForm):
    class Meta:
        model = Tendencias
        fields = ["indicador", "periodo", "porcentaje_variacion", "interpretacion"]


class ActividadForm(BaseBootstrapForm):
    class Meta:
        model = Actividad
        fields = ["actor", "accion", "entidad_afectada", "detalles"]


class PublicaForm(BaseBootstrapForm):
    class Meta:
        model = Publica
        fields = ["titulo", "contenido", "es_visible"]


class PrivadaForm(BaseBootstrapForm):
    class Meta:
        model = Privada
        fields = ["titulo", "contenido_sensible", "perfil_autorizado"]