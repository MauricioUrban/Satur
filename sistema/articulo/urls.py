from django.urls import path
from . import views
#para poder manejar las imagenes
from django.conf import settings
#ruta estatica que vamos a requerir para las imagenes
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('articulos', views.articulos, name='articulos'),
    path('articulos/crear', views.crear, name='crear'),
    path('articulos/editar', views.editar, name='editar'),

#para manejo de imagenes
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


