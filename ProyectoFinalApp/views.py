from django.shortcuts import render
from carrito.carrito import Carrito  

# Create your views here.

def index(request):  
    carrito = Carrito(request)
    return render(request,'index.html')

def nosotros(request):
    return render(request,'nosotros.html')

def login(request):
    return render(request,'login.html')