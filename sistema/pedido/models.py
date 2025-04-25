from django.db import models
from django.forms import ValidationError

# Create your models here.

# para mostrar el nombre del producto en el admin
# OJO no esta funcionando bien
def __str__(self):
        return f"Pedido: {self.id} - Cliente: {self.cliente} - Empresa: {self.empresa} - Cant Pallets: {self.cant_pallets}"

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name="Fecha")
    empresa = models.CharField(max_length=30, verbose_name="Empresa")
    cliente = models.CharField(max_length=30, verbose_name="Cliente")
    destino = models.CharField(max_length=30, verbose_name="Destino")
    cant_pallets = models.DecimalField(max_digits=3, decimal_places=1)
    demora = models.CharField(max_length=30, null=True, blank=True, verbose_name="Demora")
    observacion = models.TextField(null=True, blank=True, verbose_name="Observación")

    def clean(self):
        if self.cant_pallets <= 0:
            raise ValidationError("La cantidad de pallets debe ser mayor a 0.")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
