from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="nombre clave", max_length=100, unique=True)
    nombre = models.CharField(verbose_name="red social")
    url = models.URLField(max_length=200, null=True, blank=True, verbose_name="Enlace")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre