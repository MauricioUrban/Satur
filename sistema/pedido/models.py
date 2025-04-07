from django.db import models
from django.forms import ValidationError

# Create your models here.

# para mostrar el nombre del producto en el admin
# OJO no esta funcionando bien
def __str__(self):
    fila = "Producto: " + self.producto + " - " + "Presentacion: " + self.presentacion + "Marca: " + self.marca + " - " + "Precio: " + str(self.precio)
    return fila

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    empresa = models.CharField(max_length=30, verbose_name="Empresa")
    cliente = models.CharField(max_length=30, verbose_name="Cliente")
    destino = models.CharField(max_length=30, verbose_name="Destino")
    cant_pallets = models.DecimalField(max_digits=3, decimal_places=1)
    demora = models.CharField(max_length=30)
    observacion = models.CharField(max_length=30)
    
