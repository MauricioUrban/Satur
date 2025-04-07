from django.db import models
from django.forms import ValidationError

# Restricción de longitud para el campo EAN
def validar_longitud_ean(value):
    if len(value) != 13:
        raise ValidationError('El EAN debe tener 13 caracteres.')   
    
# Restricción de longitud para el campo DUN
def validar_longitud_dun(value):
    if len(value) != 14:
        raise ValidationError('El EAN debe tener 14 caracteres.')   
    
# para mostrar el nombre del producto en el admin
# OJO no esta funcionando bien
def __str__(self):
    fila = "Producto: " + self.producto + " - " + "Presentacion: " + self.presentacion + "Marca: " + self.marca + " - " + "Precio: " + str(self.precio)
    return fila

# para borrar la imagen del disco también
def delete(self, using=None, keep_parents=False):
    self.imagen.storage.delete(self.imagen.name)
    super().delete()
class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    ean = models.CharField(max_length=13)
    dun = models.CharField(max_length=14)
    imagen = models.ImageField(upload_to="imagenes/", verbose_name="Imagen", null=True)
    # verbose me permite mostrar el producto en este caso
    producto = models.CharField(max_length=30, verbose_name="Producto")
    presentacion = models.CharField(max_length=30, verbose_name="Presentacion")
    uxb = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = precio = models.DecimalField(max_digits=10, decimal_places=2)
    departamento = models.CharField(max_length=30)
    familia = models.CharField(max_length=30)
    acciones = models.CharField(max_length=30)

