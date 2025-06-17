from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


class Categoria(models.Model):
    
    nombre= models.CharField(max_length=70)

    def __str__(self):
        return f"{self.nombre}"

class Presupuesto(models.Model):
    usuario  = models.OneToOneField(User, on_delete=models.CASCADE)
    monto_maximo = models.DecimalField(max_digits=12, decimal_places=2) 
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_expiracion = models.DateTimeField()
    
    class Meta:
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Presupuestos'
        ordering = ['-fecha_de_expiracion']

    
    def __str__(self):
        return f"Presupuesto de {self.usuario} - {self.fecha_de_expiracion.strftime('%B %Y')}"

class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True)
    descripcion = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.monto} - {self.categoria}"