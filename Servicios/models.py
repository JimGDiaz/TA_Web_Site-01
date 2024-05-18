
from django.db import models

# Create your models here.
class Servicios(models.Model):
    
    titulo = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    persona_funcion = models.CharField(max_length=75)
    contenido = models.TextField('Contenido:', max_length=360)
    imagen = models.ImageField(upload_to='servicios_media')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add = True)
    
    class Meta():
        verbose_name='servicio'
        verbose_name_plural='servicios'
        
    def __str__(self):
        return 'Proyecto: %s - Tipo: %s' %(self.nombre, self.titulo)

