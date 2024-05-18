from django.db import models

# Create your models here.
class Uso_Edif(models.Model):
    
    genero = models.CharField(max_length=30)
    sub_genero=models.CharField(max_length=36)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add = True)
    
    class Meta():
        verbose_name='uso_Edif'
        verbose_name_plural='usos_Edif'
        
    def __str__(self):
        return '%s\n ->%s' %(self.genero, self.sub_genero)
        
class Prytos_Realizados(models.Model):
    
    nombre = models.CharField(max_length=45)
    persona_funcion = models.CharField(max_length=75)
    ubicacion=models.CharField(max_length=60)
    descripcion = models.TextField('Contenido:', max_length=300)
    imagen_D = models.ImageField(upload_to='prytos_realizados_media')
    imagen_A = models.ImageField(upload_to='prytos_realizados_media')
    usos= models.ForeignKey(Uso_Edif, on_delete=models.CASCADE) # Sí se elimina un Uso se eliminan las obras relacionadas
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now_add = True)
    
    class Meta():
        verbose_name='pryto_realizado'
        verbose_name_plural='prytos_realizados'
        
    def __str__(self):
        return 'Nombre: %s => Ubicación: %s' %(self.nombre, self.ubicacion)