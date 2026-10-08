from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Perfil, Actor, Estado, Gestion, Operacion, Datos,
    Antecedentes, Excepcionales, Reglas, Consultas, Reportes,
    Indicador, Tendencias, Actividad, Publica, Privada
)
from .serializer import (
    PerfilSerializer, ActorSerializer, EstadoSerializer, GestionSerializer,
    OperacionSerializer, DatosSerializer, AntecedentesSerializer,
    ExcepcionalesSerializer, ReglasSerializer, ConsultasSerializer,
    ReportesSerializer, IndicadorSerializer, TendenciasSerializer,
    ActividadSerializer, PublicaSerializer, PrivadaSerializer
)

def index(request):
    return render(request, 'index.html')

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class GestionViewSet(viewsets.ModelViewSet):
    queryset = Gestion.objects.all()
    serializer_class = GestionSerializer

class OperacionViewSet(viewsets.ModelViewSet):
    queryset = Operacion.objects.all()
    serializer_class = OperacionSerializer

class DatosViewSet(viewsets.ModelViewSet):
    queryset = Datos.objects.all()
    serializer_class = DatosSerializer

class AntecedentesViewSet(viewsets.ModelViewSet):
    queryset = Antecedentes.objects.all()
    serializer_class = AntecedentesSerializer

class ExcepcionalesViewSet(viewsets.ModelViewSet):
    queryset = Excepcionales.objects.all()
    serializer_class = ExcepcionalesSerializer

class ReglasViewSet(viewsets.ModelViewSet):
    queryset = Reglas.objects.all()
    serializer_class = ReglasSerializer

class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer

class ReportesViewSet(viewsets.ModelViewSet):
    queryset = Reportes.objects.all()
    serializer_class = ReportesSerializer

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class TendenciasViewSet(viewsets.ModelViewSet):
    queryset = Tendencias.objects.all()
    serializer_class = TendenciasSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class PublicaViewSet(viewsets.ModelViewSet):
    queryset = Publica.objects.all()
    serializer_class = PublicaSerializer

class PrivadaViewSet(viewsets.ModelViewSet):
    queryset = Privada.objects.all()
    serializer_class = PrivadaSerializer