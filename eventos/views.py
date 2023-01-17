from django.shortcuts import render
from .models import Post

# Create your views here.

def eventos(request):
    posts = Post.objects.all()
    return render(request,'eventos/eventos.html',{'posts':posts})   