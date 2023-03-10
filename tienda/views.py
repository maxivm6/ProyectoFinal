from django.shortcuts import render, redirect
from . models import *
from carrito.carrito import Carrito
from django.contrib.auth.decorators import login_required 

# Create your views here.

def producto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,'tienda/tienda.html',{'categorias':categorias,'productos':productos})

def categoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria_id)
    return render(request,'tienda/categorias.html',{'categoria':categoria,'productos':productos})


@login_required (login_url="/autenticacion/")
def agregar_tienda(request,producto_id):
        carrito = Carrito(request)
        producto = Producto.objects.get(id=producto_id)
        carrito.agregar(producto=producto)
        return redirect('producto')

