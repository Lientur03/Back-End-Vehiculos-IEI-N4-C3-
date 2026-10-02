from django.urls import path, include
from rest_framework import routers
from vehiculos import views

enrutador = routers.DefaultRouter()

enrutador.register(r'perfiles', views.)
enrutador.register(r'')

urlpatterns = [
    path('', include(enrutador.urls)),
]