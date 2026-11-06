from django.urls import path, include
from rest_framework import routers
from vehiculos import views

enrutador = routers.DefaultRouter()


urlpatterns = [
    path('', include(enrutador.urls)),
    path('index/', views.index, name='index'),
]