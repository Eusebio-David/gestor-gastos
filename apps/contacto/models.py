from django.db import models

# Create your models here.
class InformacionContacto(models.Model):
    """
    Creamos una base de datos, para poder guardar informacíon del contacto empresarial, pudiendo modificarlo cuando se necesite.
    Solo funcionaran a modo informativo, no se realizan acciones con estos campos. 
    """

    DIAS_SEMANAS = {
        'LU':'Lunes',
        'MA': 'Martes',
        'MI': 'Miércoles',
        'JU': 'Jueves',
        'VI': 'Viernes',
        'SA': 'Sábado',
        'DO':'Domingo'
    }
    email = models.EmailField(max_length=200, blank=False, null=False, verbose_name='Email Empresa' )
    telefono_empresa = models.CharField(max_length=20, blank=False, null=False, verbose_name='Teléfono')
    direccion = models.CharField(max_length = 40, blank=False, null=False, verbose_name='Dirección')
    dias = models.CharField(max_length=3, choices=DIAS_SEMANAS)
    dias_hasta = models.CharField(max_length=3, choices=DIAS_SEMANAS, default='V', verbose_name='Hasta Días')
    hora_apertura = models.IntegerField(choices=[(i, f'{i}:00') for i in range(0,24)], null=False, blank=False, verbose_name='Horario apertura')
    hora_cierre = models.IntegerField(choices=[(i,f'{i}:00') for i in range(0,24)], verbose_name='Hora de cierre', null=False, blank=False)
    hora_apertura_sabado = models.IntegerField(choices=[(i, f'{i}:00') for i in range(0,24)], null=False, blank=False, default=10, verbose_name='Horario apertura')
    hora_cierre_sabado = models.IntegerField(choices=[(i,f'{i}:00') for i in range(0,24)], verbose_name='Hora de cierre', null=False, blank=False, default=2)


    def __str__(self):
        return "Contacto oficial"

    class Meta:
        verbose_name = "Información de contacto"
        verbose_name_plural = "Información de contacto"