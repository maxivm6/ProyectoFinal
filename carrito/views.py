from django.shortcuts import render,redirect
from .carrito import Carrito
from tienda.models import Producto

def carrito(request):
    return render(request,'carrito/carrito.html')

def agregar(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregar(producto=producto)
    
    return redirect('carrito')

def eliminar(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.eliminar(producto=producto)
    
    return redirect('producto')

def restar(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.restar_producto(producto=producto)
    
    return redirect('carrito')

def limpiar(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    
    return redirect('carrito')