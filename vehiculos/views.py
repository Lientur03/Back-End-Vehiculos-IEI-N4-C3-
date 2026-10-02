from django.shortcuts import render
from rest_framework import viewsets

from .models import Perfil, Actor, Estado, Gestion, Operacion, Datos, Antecedente, Excepcionales, Reglas, Consultas, Reportes 
from .models import Indicador, Tendencias, Actividad, Publica, Privada

from .serializer import PerfilSerializer, ActorSerializer, EstadoSerializer, GestionSerializer, OperacionSerializer, DatosSerializer, AntecedentesSerializer

from .serializer import ExcepcionalesSerializer, ReglasSerializer, ConsultasSerializer, ReportesSerializer, IndicadorSerializer, TendenciasSerializer

from .serializer import ActividadSerializer, PublicaSerializer, PrivadaSerializer

def index(request):
    return render(request, 'index.html')

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer