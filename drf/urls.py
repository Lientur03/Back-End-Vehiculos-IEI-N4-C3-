from django.contrib import admin
from django.urls import path, include
from vehiculos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('vehiculos/', include('vehiculos.urls')),
    path('api-auth/', include('rest_framework.urls')),
]