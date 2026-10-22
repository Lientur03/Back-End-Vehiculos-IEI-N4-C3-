from django.db import models
from django.contrib.auth.models import User

# 1. Perfil de usuario y niveles de acceso
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(
        max_length=50, 
        choices=[('CONDUCTOR', 'Conductor'), ('TALLER', 'Taller'), ('ADMIN', 'Administrador')]
    )
    nivel_acceso = models.IntegerField(default=1)
    departamento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"

# 2. Modelo Del Rol Administrador
class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True, max_length=100)
    
    def __str__(self):
        return self.nombre

# 3. Modelo Del Rol Supervisor
class Supervisor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True, max_length=100)
    perfil = models.CharField(max_length=50, default='Supervisor')
    
    def __str__(self):
        return self.nombre

# 4. Cliente que va al Taller De Mecánica Automotriz (Antes Actor)
class Cliente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True, max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

# 5. Modelo Principal sobre los Vehiculos
class Vehiculos(models.Model):
    patente = models.CharField(max_length=10, primary_key=True, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    tipo_combustible = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"

# 6. Estados de flota y mantenimiento
class Estado(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# 7. Gestión global de flotas y asignaciones
class Gestion(models.Model):
    codigo_flota = models.CharField(max_length=50, unique=True)
    nombre_area = models.CharField(max_length=100)
    responsable = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name='gestiones')
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Gestión {self.codigo_flota} - {self.nombre_area}"

# 8. Operaciones de vehículos y servicios
class Operacion(models.Model):
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, related_name='operaciones', null=True, blank=True)
    actor = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='operaciones')
    patente_vehiculo = models.CharField(max_length=10)
    tipo_operacion = models.CharField(
        max_length=50, 
        choices=[('USO_DIARIO', 'Uso Diario'), ('MANTENCION', 'Mantención Preventiva'), ('REPARACION', 'Reparación Correctiva')]
    )
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Operación {self.id} - {self.patente_vehiculo} ({self.tipo_operacion})"

# 9. Registros de datos y telemetría
class Datos(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name='datos_registrados')
    kilometraje = models.PositiveIntegerField()
    nivel_combustible = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Datos {self.id} - KM: {self.kilometraje}"

# 10. Antecedentes históricos de vehículos
class Antecedentes(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE, related_name='antecedentes')
    fecha_evento = models.DateField()
    tipo_antecedente = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo_adjunto = models.FileField(upload_to='antecedentes/', null=True, blank=True)

    def __str__(self):
        return f"Antecedente {self.vehiculo.patente} - {self.tipo_antecedente}"

# 11. Registro de situaciones excepcionales o incidencias
class Excepcionales(models.Model):
    operacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name='excepciones')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    nivel_prioridad = models.CharField(
        max_length=20, 
        choices=[('BAJA', 'Baja'), ('MEDIA', 'Media'), ('ALTA', 'Alta'), ('CRITICA', 'Crítica')]
    )
    resuelto = models.BooleanField(default=False)
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Excepción: {self.titulo} [{self.nivel_prioridad}]"

# 12. Reglas de negocio e integridad del sistema
class Reglas(models.Model):
    nombre_regla = models.CharField(max_length=100)
    limite_kilometros_mantencion = models.PositiveIntegerField()
    dias_maximo_revision = models.PositiveIntegerField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_regla

# 13. Consultas avanzadas y filtros guardados
class Consultas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_consulta = models.CharField(max_length=100)
    criterios_busqueda = models.JSONField(help_text="Filtros guardados en formato JSON")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_consulta

# 14. Reportes generados
class Reportes(models.Model):
    titulo = models.CharField(max_length=150)
    tipo_reporte = models.CharField(max_length=50)
    generado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    parametros_usados = models.TextField(blank=True)

    def __str__(self):
        return f"Reporte: {self.titulo} ({self.fecha_generacion.strftime('%Y-%m-%d')})"

# 15. Indicadores de gestión (KPIs)
class Indicador(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    unidad_medida = models.CharField(max_length=20)
    fecha_calculo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}: {self.valor} {self.unidad_medida}"

# 16. Análisis de tendencias
class Tendencias(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, related_name='tendencias')
    periodo = models.CharField(max_length=20)
    porcentaje_variacion = models.DecimalField(max_digits=5, decimal_places=2)
    interpretacion = models.TextField()

    def __str__(self):
        return f"Tendencia {self.periodo} - {self.indicador.nombre}"

# 17. Auditoría y registro de actividad
class Actividad(models.Model):
    actor = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=150)
    entidad_afectada = models.CharField(max_length=50)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    detalles = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fecha_hora} - {self.actor}: {self.accion}"

# 18. Información pública
class Publica(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    es_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

# 19. Información privada / restringida
class Privada(models.Model):
    titulo = models.CharField(max_length=150)
    contenido_sensible = models.TextField()
    perfil_autorizado = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[PRIVADO] {self.titulo}"