from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    
    nombre = models.CharField(max_length=45)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add = True)
    
    class Meta():
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nombre
        
class Post(models.Model):

    titulo = models.CharField(max_length=45)
    contenido = models.CharField(max_length=240)
    imagen = models.ImageField(upload_to='blog_media')
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add = True)
    
    class Meta():
        verbose_name='post'
        verbose_name_plural='posts'