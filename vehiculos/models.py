from django.db import models
from django.contrib.auth.models import User

str_nombre = "Nombre"
str_correo = "Correo Electrónico"
str_telefono = "Teléfono"
str_direccion = "Dirección"
str_descripcion = "Descripción"
str_titulo = "Título"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"


# 1. Perfil de usuario y niveles de acceso
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil', verbose_name="Usuario")
    rol = models.CharField(
        "Rol",
        max_length=50,
        choices=[('CONDUCTOR', 'Conductor'), ('TALLER', 'Taller'), ('ADMIN', 'Administrador')]
    )
    nivel_acceso = models.IntegerField("Nivel de Acceso", default=1)
    departamento = models.CharField("Departamento", max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"

    class Meta:
        db_table_comment = "Perfiles de usuario, roles y niveles de acceso del sistema."


# 2. Modelo Del Rol Administrador
class Administrador(models.Model):
    nombre = models.CharField(str_nombre, max_length=100)
    correo = models.EmailField(str_correo, unique=True, max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table_comment = "Registro de usuarios con rol de administrador."


# 3. Modelo Del Rol Supervisor
class Supervisor(models.Model):
    nombre = models.CharField(str_nombre, max_length=100)
    correo = models.EmailField(str_correo, unique=True, max_length=100)
    perfil = models.CharField("Perfil", max_length=50, default='Supervisor')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table_comment = "Registro de usuarios con rol de supervisor."


# 4. Cliente que va al Taller De Mecánica Automotriz (Antes Actor)
class Cliente(models.Model):
    rut = models.CharField("RUT", max_length=12, primary_key=True, unique=True)
    nombre = models.CharField(str_nombre, max_length=100)
    correo = models.EmailField(str_correo, unique=True, max_length=100)
    telefono = models.CharField(str_telefono, max_length=20)
    direccion = models.CharField(str_direccion, max_length=255)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

    class Meta:
        db_table_comment = "Clientes y actores asociados a vehículos y operaciones."


# 5. Modelo Principal sobre los Vehiculos
class Vehiculos(models.Model):
    patente = models.CharField("Patente", max_length=10, primary_key=True, unique=True)
    marca = models.CharField("Marca", max_length=50)
    modelo = models.CharField("Modelo", max_length=50)
    anio = models.IntegerField("Año")
    tipo_combustible = models.CharField("Tipo de Combustible", max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos', verbose_name="Cliente")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

    class Meta:
        db_table_comment = "Entidad principal de vehículos registrados en el sistema."


# 6. Estados de flota y mantenimiento
class Estado(models.Model):
    nombre = models.CharField(str_nombre, max_length=50, unique=True)
    descripcion = models.TextField(str_descripcion, blank=True)
    es_activo = models.BooleanField("Es Activo", default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table_comment = "Estados operativos de flota y mantenimiento."


# 7. Gestión global de flotas y asignaciones
class Gestion(models.Model):
    codigo_flota = models.CharField("Código de Flota", max_length=50, unique=True)
    nombre_area = models.CharField("Nombre del Área", max_length=100)
    responsable = models.ForeignKey(
        Cliente, on_delete=models.SET_NULL, null=True, related_name='gestiones', verbose_name="Responsable"
    )
    fecha_inicio = models.DateField("Fecha de Inicio")
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return f"Gestión {self.codigo_flota} - {self.nombre_area}"

    class Meta:
        db_table_comment = "Gestión global de flotas y asignaciones."


# 8. Operaciones de vehículos y servicios
class Operacion(models.Model):
    gestion = models.ForeignKey(
        Gestion, on_delete=models.CASCADE, related_name='operaciones', null=True, blank=True, verbose_name="Gestión"
    )
    actor = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='operaciones', verbose_name="Actor")
    patente_vehiculo = models.CharField("Patente Vehículo", max_length=10)
    tipo_operacion = models.CharField(
        "Tipo de Operación",
        max_length=50,
        choices=[('USO_DIARIO', 'Uso Diario'), ('MANTENCION', 'Mantención Preventiva'), ('REPARACION', 'Reparación Correctiva')]
    )
    fecha_inicio = models.DateTimeField("Fecha de Inicio")
    fecha_fin = models.DateTimeField("Fecha de Fin", null=True, blank=True)
    observaciones = models.TextField("Observaciones", blank=True)

    def __str__(self):
        return f"Operación {self.id} - {self.patente_vehiculo} ({self.tipo_operacion})"

    class Meta:
        db_table_comment = "Operaciones de uso, mantención y reparación de vehículos."


# 9. Registros de datos y telemetría
class Datos(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name='datos_registrados', verbose_name="Operación")
    kilometraje = models.PositiveIntegerField("Kilometraje")
    nivel_combustible = models.DecimalField("Nivel de Combustible", max_digits=5, decimal_places=2)
    fecha_registro = models.DateTimeField("Fecha de Registro", auto_now_add=True)

    def __str__(self):
        return f"Datos {self.id} - KM: {self.kilometraje}"

    class Meta:
        db_table_comment = "Registros de telemetría, kilometraje y combustible."


# 10. Antecedentes históricos de vehículos
class Antecedentes(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE, related_name='antecedentes', verbose_name="Vehículo")
    fecha_evento = models.DateField("Fecha del Evento")
    tipo_antecedente = models.CharField("Tipo de Antecedente", max_length=100)
    descripcion = models.TextField(str_descripcion)
    archivo_adjunto = models.FileField("Archivo Adjunto", upload_to='antecedentes/', null=True, blank=True)

    def __str__(self):
        return f"Antecedente {self.vehiculo.patente} - {self.tipo_antecedente}"

    class Meta:
        db_table_comment = "Historial de eventos y antecedentes de cada vehículo."


# 11. Registro de situaciones excepcionales o incidencias
class Excepcionales(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name='excepciones', verbose_name="Operación")
    titulo = models.CharField(str_titulo, max_length=150)
    descripcion = models.TextField(str_descripcion)
    nivel_prioridad = models.CharField(
        "Nivel de Prioridad",
        max_length=20,
        choices=[('BAJA', 'Baja'), ('MEDIA', 'Media'), ('ALTA', 'Alta'), ('CRITICA', 'Crítica')]
    )
    resuelto = models.BooleanField("Resuelto", default=False)
    fecha_reporte = models.DateTimeField("Fecha de Reporte", auto_now_add=True)

    def __str__(self):
        return f"Excepción: {self.titulo} [{self.nivel_prioridad}]"

    class Meta:
        db_table_comment = "Situaciones excepcionales o incidencias reportadas en operaciones."


# 12. Reglas de negocio e integridad del sistema
class Reglas(models.Model):
    nombre_regla = models.CharField("Nombre de Regla", max_length=100)
    limite_kilometros_mantencion = models.PositiveIntegerField("Límite Kilómetros Mantención")
    dias_maximo_revision = models.PositiveIntegerField("Días Máximo Revisión")
    activa = models.BooleanField("Activa", default=True)

    def __str__(self):
        return self.nombre_regla

    class Meta:
        db_table_comment = "Reglas de negocio para mantención y revisión."


# 13. Consultas avanzadas y filtros guardados
class Consultas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    nombre_consulta = models.CharField("Nombre de Consulta", max_length=100)
    criterios_busqueda = models.JSONField("Criterios de Búsqueda", help_text="Filtros guardados en formato JSON")
    fecha_creacion = models.DateTimeField(str_fecha_creacion, auto_now_add=True)

    def __str__(self):
        return self.nombre_consulta

    class Meta:
        db_table_comment = "Consultas y filtros guardados por usuario."


# 14. Reportes generados
class Reportes(models.Model):
    titulo = models.CharField(str_titulo, max_length=150)
    tipo_reporte = models.CharField("Tipo de Reporte", max_length=50)
    generado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Generado Por")
    fecha_generacion = models.DateTimeField("Fecha de Generación", auto_now_add=True)
    parametros_usados = models.TextField("Parámetros Usados", blank=True)

    def __str__(self):
        return f"Reporte: {self.titulo} ({self.fecha_generacion.strftime('%Y-%m-%d')})"

    class Meta:
        db_table_comment = "Reportes generados en el sistema."


# 15. Indicadores de gestión (KPIs)
class Indicador(models.Model):
    nombre = models.CharField(str_nombre, max_length=100)
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    unidad_medida = models.CharField("Unidad de Medida", max_length=20)
    fecha_calculo = models.DateTimeField("Fecha de Cálculo", auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}: {self.valor} {self.unidad_medida}"

    class Meta:
        db_table_comment = "Indicadores clave de gestión (KPIs)."


# 16. Análisis de tendencias
class Tendencias(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, related_name='tendencias', verbose_name="Indicador")
    periodo = models.CharField("Período", max_length=20)
    porcentaje_variacion = models.DecimalField("Porcentaje de Variación", max_digits=5, decimal_places=2)
    interpretacion = models.TextField("Interpretación")

    def __str__(self):
        return f"Tendencia {self.periodo} - {self.indicador.nombre}"

    class Meta:
        db_table_comment = "Análisis de tendencias a partir de indicadores."


# 17. Auditoría y registro de actividad
class Actividad(models.Model):
    actor = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, verbose_name="Actor")
    accion = models.CharField("Acción", max_length=150)
    entidad_afectada = models.CharField("Entidad Afectada", max_length=50)
    fecha_hora = models.DateTimeField("Fecha y Hora", auto_now_add=True)
    detalles = models.TextField("Detalles", blank=True)

    def __str__(self):
        return f"{self.fecha_hora} - {self.actor}: {self.accion}"

    class Meta:
        db_table_comment = "Bitácora de auditoría y actividad del sistema."


# 18. Información pública
class Publica(models.Model):
    titulo = models.CharField(str_titulo, max_length=150)
    contenido = models.TextField("Contenido")
    fecha_publicacion = models.DateTimeField("Fecha de Publicación", auto_now_add=True)
    es_visible = models.BooleanField("Es Visible", default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table_comment = "Información pública disponible en la aplicación."


# 19. Información privada / restringida
class Privada(models.Model):
    titulo = models.CharField(str_titulo, max_length=150)
    contenido_sensible = models.TextField("Contenido Sensible")
    perfil_autorizado = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Perfil Autorizado")
    fecha_registro = models.DateTimeField("Fecha de Registro", auto_now_add=True)

    def __str__(self):
        return f"[PRIVADO] {self.titulo}"

    class Meta:
        db_table_comment = "Información privada o restringida por perfil."