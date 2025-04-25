from django.http import HttpResponse
from .models import Pedido
from .forms import PedidoForm
from django.shortcuts import render, redirect


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/index.html', {'pedidos': pedidos})

def crear(request):
    formulario = PedidoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('pedidos')

    return render(request, 'pedidos/crear.html', {'formulario': formulario})

def editar(request, id):
    pedido = Pedido.objects.get(id=id)
    formulario = PedidoForm(request.POST or None, request.FILES or None, instance=pedido)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('pedidos')    
    return render(request, 'pedidos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect('pedidos')
