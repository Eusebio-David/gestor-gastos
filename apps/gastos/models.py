from django.db import models
from decimal import Decimal


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=70, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Categoria(models.Model):
    
    nombre= models.CharField(max_length=70)

    def __str__(self):
        return f"{self.nombre}"

class Presupuesto(models.Model):
    usuario  = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    monto_maximo = models.DecimalField(max_digits=12, decimal_places=2) 
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_expiracion = models.DateTimeField()

    def __str__(self):
        return f"Presupuesto de {self.usuario.nombre}"

class Gasto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True)
    descripcion = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.monto} - {self.categoria}"