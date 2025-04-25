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
    path('articulos/crear', views.crear, name='articulo_crear'),
    path('articulos/eliminar/<int:id>', views.eliminar, name='articulo_eliminar'),
    path('articulos/editar/<int:id>', views.editar, name='articulo_editar'),


#para manejo de imagenes
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
