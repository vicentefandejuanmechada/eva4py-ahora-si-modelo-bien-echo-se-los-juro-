from django.db import models

# Create your models here.
class Producto(models.Model):
    codproducto = models.CharField(max_length=50)
    nombreproducto = models.CharField(max_length=100)
    provedor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    cantidad_x_unidad =models.CharField(max_length=50)
    valor_peso = models.CharField(max_length=50)
    valor_euro = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)

class clientes(models.Model):
    rut=models.CharField(max_length=25)
    numero_cliente=models.TextField(max_length=50)
    fecha_registro=models.CharField(max_length=50)
    apellido_p=models.CharField(max_length=60)
    apellido_m=models.CharField(max_length=60)
    nombre=models.TextField(max_length=50)  
    correo=models.CharField(max_length=100) 
    fecha_nacimiento=models.CharField(max_length=25) 
    telefono=models.CharField(max_length=25) 

class venta(models.Model):
    boleta=models.CharField(max_length=50)
    Producto=models.CharField(max_length=50) 
    cantidad=models.CharField(max_length=50) 
    venta_bruto=models.CharField(max_length=50) 
    iva=models.CharField(max_length=50) 
    total_venta=models.CharField(max_length=50)  