from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/crear/', views.crear, name='crear'),
    path('pedidos/editar/<int:id>/', views.editar, name='editar'),
    path('pedidos/eliminar/<int:id>/', views.eliminar, name='eliminar'),
]