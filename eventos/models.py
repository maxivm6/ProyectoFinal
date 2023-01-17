from django.db import models

# Create your models here.

class Post(models.Model):
    titulo=models.CharField(max_length=40)
    imagen=models.ImageField()
    contenido=models.CharField(max_length=800)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self): return self.titulo
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'