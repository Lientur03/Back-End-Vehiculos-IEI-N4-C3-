from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from vehiculos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('vehiculos/', include('vehiculos.urls'))
]

# Forzar la entrega de archivos estáticos incluso cuando DEBUG = False
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.BASE_DIR / 'vehiculos' / 'static'}),
]