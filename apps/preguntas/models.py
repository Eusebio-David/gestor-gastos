from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags
# Create your models here.

class PreguntasFrecuentes(models.Model):
    CATEGORIA = [('USO', 'Uso de la app'),
                 ('CUENTA','Cuenta'),
                 ('TECNICO','Soporte técnico'),
                 ('GENERAL','General')]
    
    titulo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Título')
    contenido = RichTextField(verbose_name='contenido', default='contenido pendiente')
    categoria = models.CharField(max_length=20,choices=CATEGORIA, verbose_name='Categorías')
    orden = models.PositiveIntegerField(default=0, verbose_name='Orden')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacón')

    class Meta:
        ordering = ['orden','-fecha_creacion']


    def resumen(self):
        # Elimina etiquetas HTML, divide en párrafos y toma los primeros 3
        texto_plano = strip_tags(self.contenido)
        parrafos = texto_plano.split('\n')
        primeros_7 = parrafos[:7]
        return '\n\n'.join(primeros_7)

    def __str__(self):
        return self.titulo