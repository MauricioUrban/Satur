from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pedidos', views.pedidos, name='pedidos'),
    path('pedidos/crear', views.crear, name='crear'),
    path('pedidos/editar', views.editar, name='editar'),
    path('pedidos/<int:id>', views.eliminar, name='eliminar'),
    path('pedidos/editar/<int:id>', views.editar, name='editar'),
]