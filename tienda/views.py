from django.shortcuts import render, redirect
from . models import *
from carrito.carrito import Carrito

# Create your views here.

def producto(request):
    productos = Producto.objects.all()
    return render(request,'tienda/tienda.html',{'productos':productos})

def categoria(request,categoria_id):
    categorias = Categoria.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria_id)
    return render(request,'tienda/tienda.html',{'categorias':categorias},{'productos':productos})

def agregar_tienda(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregar(producto=producto)
    
    return redirect('producto')