from django.contrib import admin
from .models import *

# Register your models here.

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
admin.site.register(Producto,ProductosAdmin)
admin.site.register(Categoria,CategoriasAdmin)