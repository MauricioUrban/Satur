from django.http import HttpResponse
from .models import Pedido
from .forms import PedidoForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.db.models import Sum

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def pedidos(request):
    orden = request.GET.get('orden', 'id')  # Orden predeterminado
    filtro_destinos = request.GET.getlist('filtro_destinos')  # Obtener lista de destinos seleccionados
    filtro_empresa = request.GET.get('filtro_empresa', '')  # Valor del filtro por empresa

    # Obtener destinos únicos disponibles en la base de datos
    destinos_disponibles = Pedido.objects.values_list('destino', flat=True).distinct().order_by('destino')


    # Recuperar todos los pedidos y ordenarlos
    pedidos = Pedido.objects.all().order_by(orden)

    # Filtrar por los destinos seleccionados si hay al menos uno marcado
    if filtro_destinos:
        pedidos = pedidos.filter(destino__in=filtro_destinos)

    if filtro_empresa:
        pedidos = pedidos.filter(empresa__icontains=filtro_empresa)

    # Calcular la cantidad total de pallets
    total_pallets = pedidos.aggregate(Sum('cant_pallets'))['cant_pallets__sum'] or 0   

    return render(request, 'pedidos/index.html', {
        'pedidos': pedidos,
        'filtro_destinos': filtro_destinos,
        'filtro_empresa': filtro_empresa,
        'destinos_disponibles': destinos_disponibles,
        'orden_actual': orden,
        'total_pallets': total_pallets  # Se envía el total a la plantilla
    })

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