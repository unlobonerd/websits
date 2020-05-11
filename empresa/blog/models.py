from django.db import models  #para los modelos osea tabals de la db
from django.utils.timezone import now #para importar la zona horaria
from django.contrib.auth.models import User  #para importar los usuarios del panel de admisnitracion de django
# Create your models here.

class Category(models.Model):
    name    = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edicion')
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicacioin", default=now)
    image = models.ImageField(verbose_name = 'Imagen', upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)     #creamso una llave foranea al usuario
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts") #aqui s erelaciona la tabal category con una instruccion muchos a muchos
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de Creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edicion')
    
    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ["-created"]

    def __str__(self):
        return self.title
