from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self): return self.nombre    


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='tienda',blank=True,null=True)
    precio = models.IntegerField()
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        
    def __str__(self): return self.nombre