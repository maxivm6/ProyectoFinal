from django.shortcuts import render
from .models import Post

# Create your views here.

def eventos(request):
    posts = Post.objects.all()
    return render(request,'eventos/eventos.html',{'posts':posts})

def mostrar_evento(request,post_id):
    post = Post.objects.get( id = post_id)
    return render(request,'eventos/evento.html',{'post':post})   