from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulos/index.html', {'articulos': articulos})

def crear(request):
    return render(request, 'articulos/crear.html')
def editar(request):
    return render(request, 'articulos/editar.html')











