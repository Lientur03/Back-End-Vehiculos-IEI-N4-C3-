from rest_framework import serializers
from .models import (
    Perfil, Actor, Estado, Gestion, Operacion, Datos,
    Antecedentes, Excepcionales, Reglas, Consultas, Reportes,
    Indicador, Tendencias, Actividad, Publica, Privada
)

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestion
        fields = '__all__'

class OperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operacion
        fields = '__all__'

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = '__all__'

class AntecedentesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Antecedentes
        fields = '__all__'

class ExcepcionalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excepcionales
        fields = '__all__'

class ReglasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reglas
        fields = '__all__'

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'

class ReportesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reportes
        fields = '__all__'

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'

class TendenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tendencias
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class PublicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publica
        fields = '__all__'

class PrivadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privada
        fields = '__all__'