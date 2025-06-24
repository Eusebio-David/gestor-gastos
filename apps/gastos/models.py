from django.db import models
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Sum

# Create your models here.


class Categoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=70)

    def __str__(self):
        return f"{self.nombre}"

class Presupuesto(models.Model):
    usuario  = models.OneToOneField(User, on_delete=models.CASCADE)
    monto_maximo = models.DecimalField(max_digits=12, decimal_places=2) 
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_expiracion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        verbose_name = 'Presupuesto'
        verbose_name_plural = 'Presupuestos'
        ordering = ['-fecha_de_expiracion']

    @property
    def total_gastos(self):
        """
        Obtenemos los gastos del usuario dentro del rango del presupuesto activo
        """
        gastos = Gasto.objects.filter(usuario=self.usuario,
                                      fecha_creacion__gte=self.fecha_de_creacion.date(),
                                      fecha_creacion__lte=self.fecha_de_expiracion.date())
        total = gastos.aggregate(suma=Sum('monto'))['suma'] or 0
        return total 
    

    @property
    def disponible(self):
        return self.monto_maximo - self.total_gastos
    

    def __str__(self):
        return f"Presupuesto de {self.usuario} - {self.fecha_de_expiracion.strftime('%B %Y')}"

class Gasto(models.Model):

    METODOS_PAGO = [
        ('efectivo', '💵 Efectivo'),
        ('tarjeta_debito', '💳 Tarjeta de Débito'),
        ('tarjeta_credito', '💳 Tarjeta de Crédito'),
        ('transferencia', '🏦 Transferencia Bancaria'),
        ('mercado_pago', '📱 Mercado Pago'),
        ('otro', '🧾 Otro'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(max_length=150, blank=True, null=True)

    metodo_pago = models.CharField(max_length=30,
                                   choices=METODOS_PAGO,
                                   default='efectivo')
    nota_adicionales = models.TextField(blank=True, null=True)
    archivo_adjunto = models.FileField(upload_to='gastos_archivos/',
                                       blank=True,
                                       null=True)
    

    
    
    def __str__(self):
        return f"{self.monto} - {self.categoria}"