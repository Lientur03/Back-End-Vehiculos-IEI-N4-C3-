from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculos.urls')), # O la vista de tu página de inicio
]

# Servir estáticos en entorno local independientemente del estado de DEBUG
urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'vehiculos' / 'static')