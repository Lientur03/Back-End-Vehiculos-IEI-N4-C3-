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
        widgets = {
            "usuario": forms.Select(),
            "rol": forms.Select(),
            "nivel_acceso": forms.NumberInput(attrs={"min": 1, "placeholder": "Ej: 1"}),
            "departamento": forms.TextInput(attrs={"placeholder": "Departamento o unidad..."}),
        }


class AdministradorForm(BaseBootstrapForm):
    class Meta:
        model = Administrador
        fields = ["nombre", "correo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre del administrador..."}),
            "correo": forms.EmailInput(attrs={"placeholder": "admin@ejemplo.cl"}),
        }


class SupervisorForm(BaseBootstrapForm):
    class Meta:
        model = Supervisor
        fields = ["nombre", "correo", "perfil"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre del supervisor..."}),
            "correo": forms.EmailInput(attrs={"placeholder": "supervisor@ejemplo.cl"}),
            "perfil": forms.TextInput(attrs={"placeholder": "Supervisor"}),
        }


class ClienteForm(BaseBootstrapForm):
    class Meta:
        model = Cliente
        fields = ["rut", "nombre", "correo", "telefono", "direccion"]
        widgets = {
            "rut": forms.TextInput(attrs={"placeholder": "Ej: 12.345.678-9"}),
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre o razón social..."}),
            "correo": forms.EmailInput(attrs={"placeholder": "cliente@ejemplo.cl"}),
            "telefono": forms.TextInput(attrs={"placeholder": "+56 9 ..."}),
            "direccion": forms.TextInput(attrs={"placeholder": "Dirección del cliente..."}),
        }


class VehiculosForm(BaseBootstrapForm):
    class Meta:
        model = Vehiculos
        fields = ["patente", "marca", "modelo", "anio", "tipo_combustible", "cliente"]
        widgets = {
            "patente": forms.TextInput(attrs={"placeholder": "Ej: ABCD12"}),
            "marca": forms.TextInput(attrs={"placeholder": "Marca del vehículo..."}),
            "modelo": forms.TextInput(attrs={"placeholder": "Modelo del vehículo..."}),
            "anio": forms.NumberInput(attrs={"placeholder": "Ej: 2024", "min": 1900}),
            "tipo_combustible": forms.TextInput(attrs={"placeholder": "Bencina, Diésel, Híbrido..."}),
            "cliente": forms.Select(),
        }


class EstadoForm(BaseBootstrapForm):
    class Meta:
        model = Estado
        fields = ["nombre", "descripcion", "es_activo"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre del estado..."}),
            "descripcion": forms.Textarea(attrs={"placeholder": "Descripción del estado...", "rows": 3}),
            "es_activo": forms.CheckboxInput(),
        }


class GestionForm(BaseBootstrapForm):
    class Meta:
        model = Gestion
        fields = ["codigo_flota", "nombre_area", "responsable", "fecha_inicio", "activo"]
        widgets = {
            "codigo_flota": forms.TextInput(attrs={"placeholder": "Código de flota..."}),
            "nombre_area": forms.TextInput(attrs={"placeholder": "Nombre del área..."}),
            "responsable": forms.Select(),
            "fecha_inicio": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "activo": forms.CheckboxInput(),
        }


class OperacionForm(BaseBootstrapForm):
    class Meta:
        model = Operacion
        fields = [
            "gestion", "actor", "patente_vehiculo", "tipo_operacion",
            "fecha_inicio", "fecha_fin", "observaciones"
        ]
        widgets = {
            "gestion": forms.Select(),
            "actor": forms.Select(),
            "patente_vehiculo": forms.TextInput(attrs={"placeholder": "Patente del vehículo..."}),
            "tipo_operacion": forms.Select(),
            "fecha_inicio": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "fecha_fin": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "observaciones": forms.Textarea(attrs={"placeholder": "Observaciones de la operación...", "rows": 3}),
        }


class DatosForm(BaseBootstrapForm):
    class Meta:
        model = Datos
        fields = ["operacion", "kilometraje", "nivel_combustible"]
        widgets = {
            "operacion": forms.Select(),
            "kilometraje": forms.NumberInput(attrs={"placeholder": "Kilometraje actual...", "min": 0}),
            "nivel_combustible": forms.NumberInput(attrs={"placeholder": "Ej: 75.50", "step": "0.01", "min": 0}),
        }


class AntecedentesForm(BaseBootstrapForm):
    class Meta:
        model = Antecedentes
        fields = ["vehiculo", "fecha_evento", "tipo_antecedente", "descripcion", "archivo_adjunto"]
        widgets = {
            "vehiculo": forms.Select(),
            "fecha_evento": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "tipo_antecedente": forms.TextInput(attrs={"placeholder": "Tipo de antecedente..."}),
            "descripcion": forms.Textarea(attrs={"placeholder": "Detalle del antecedente...", "rows": 3}),
            "archivo_adjunto": forms.ClearableFileInput(),
        }


class ExcepcionalesForm(BaseBootstrapForm):
    class Meta:
        model = Excepcionales
        fields = ["operacion", "titulo", "descripcion", "nivel_prioridad", "resuelto"]
        widgets = {
            "operacion": forms.Select(),
            "titulo": forms.TextInput(attrs={"placeholder": "Título del caso excepcional..."}),
            "descripcion": forms.Textarea(attrs={"placeholder": "Descripción detallada...", "rows": 3}),
            "nivel_prioridad": forms.Select(),
            "resuelto": forms.CheckboxInput(),
        }


class ReglasForm(BaseBootstrapForm):
    class Meta:
        model = Reglas
        fields = ["nombre_regla", "limite_kilometros_mantencion", "dias_maximo_revision", "activa"]
        widgets = {
            "nombre_regla": forms.TextInput(attrs={"placeholder": "Nombre de la regla..."}),
            "limite_kilometros_mantencion": forms.NumberInput(attrs={"placeholder": "Ej: 10000", "min": 0}),
            "dias_maximo_revision": forms.NumberInput(attrs={"placeholder": "Ej: 180", "min": 1}),
            "activa": forms.CheckboxInput(),
        }


class ConsultasForm(BaseBootstrapForm):
    class Meta:
        model = Consultas
        fields = ["usuario", "nombre_consulta", "criterios_busqueda"]
        widgets = {
            "usuario": forms.Select(),
            "nombre_consulta": forms.TextInput(attrs={"placeholder": "Nombre de la consulta..."}),
            "criterios_busqueda": forms.Textarea(attrs={"placeholder": '{"estado": "ACTIVO"}', "rows": 3}),
        }


class ReportesForm(BaseBootstrapForm):
    class Meta:
        model = Reportes
        fields = ["titulo", "tipo_reporte", "generado_por", "parametros_usados"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Título del reporte..."}),
            "tipo_reporte": forms.TextInput(attrs={"placeholder": "Tipo de reporte..."}),
            "generado_por": forms.Select(),
            "parametros_usados": forms.Textarea(attrs={"placeholder": "Parámetros del reporte...", "rows": 3}),
        }


class IndicadorForm(BaseBootstrapForm):
    class Meta:
        model = Indicador
        fields = ["nombre", "valor", "unidad_medida"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Nombre del indicador..."}),
            "valor": forms.NumberInput(attrs={"placeholder": "Valor numérico...", "step": "0.01"}),
            "unidad_medida": forms.TextInput(attrs={"placeholder": "Ej: km, %, días..."}),
        }


class TendenciasForm(BaseBootstrapForm):
    class Meta:
        model = Tendencias
        fields = ["indicador", "periodo", "porcentaje_variacion", "interpretacion"]
        widgets = {
            "indicador": forms.Select(),
            "periodo": forms.TextInput(attrs={"placeholder": "Ej: 2026-Q4 o Noviembre 2026..."}),
            "porcentaje_variacion": forms.NumberInput(attrs={"placeholder": "Ej: 12.50", "step": "0.01"}),
            "interpretacion": forms.Textarea(attrs={"placeholder": "Análisis de tendencia...", "rows": 3}),
        }


class ActividadForm(BaseBootstrapForm):
    class Meta:
        model = Actividad
        fields = ["actor", "accion", "entidad_afectada", "detalles"]
        widgets = {
            "actor": forms.Select(),
            "accion": forms.TextInput(attrs={"placeholder": "Acción realizada..."}),
            "entidad_afectada": forms.TextInput(attrs={"placeholder": "Entidad afectada..."}),
            "detalles": forms.Textarea(attrs={"placeholder": "Detalles de la actividad...", "rows": 3}),
        }


class PublicaForm(BaseBootstrapForm):
    class Meta:
        model = Publica
        fields = ["titulo", "contenido", "es_visible"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Título de la publicación..."}),
            "contenido": forms.Textarea(attrs={"placeholder": "Contenido público...", "rows": 4}),
            "es_visible": forms.CheckboxInput(),
        }


class PrivadaForm(BaseBootstrapForm):
    class Meta:
        model = Privada
        fields = ["titulo", "contenido_sensible", "perfil_autorizado"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Título del registro privado..."}),
            "contenido_sensible": forms.Textarea(attrs={"placeholder": "Información restringida...", "rows": 4}),
            "perfil_autorizado": forms.Select(),
        }