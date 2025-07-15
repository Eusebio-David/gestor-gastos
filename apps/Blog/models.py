from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.utils.html import strip_tags
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True) 
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='imagen_post', blank=True, null=True)
    publicado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    url_info = models.URLField(blank=True, null=True)
   
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-creado']

    def __str__(self):
        return self.titulo
    

    def resumen(self):
        # Elimina etiquetas HTML, divide en párrafos y toma los primeros 3
        texto_plano = strip_tags(self.contenido)
        parrafos = texto_plano.split('\n')
        primeros_100 = parrafos[:100]
        return '\n\n'.join(primeros_100)
    
    
    def save(self, *args, **kwargs):
        """
        ¿Qué hace este código?
        Usa slugify() para convertir el título a un slug.

        Si ya existe un post con ese slug, le agrega un número (-1, -2, etc.) hasta encontrar uno único.

        Esto evita errores por unique=True en la base de datos.
        """
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            num = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)