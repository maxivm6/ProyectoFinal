from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


# Create your views here.

@login_required
def mi_perfil(request):
    perfil = User.objects.all()
    return render(request,"usuario/mi_perfil.html",{'perfil':perfil})

@login_required
def editar_perfil(request):
    
    usuario = request.user
    
    
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion["email"]
            usuario.username = informacion["username"]
            
            hashed_pwd = make_password(informacion["password1"])
            if check_password(informacion["password1"],hashed_pwd):
                usuario.password = hashed_pwd
            
            usuario.first_name = informacion["nombre"]
            usuario.last_name = informacion["apellido"]
            
            usuario.save()
            
            messages.success (request,"Tus perfil fue modificado con éxito!")
            return render(request,"usuario/mi_perfil.html")
            
            
    else:
        miFormulario = UserEditForm(initial={"password1":usuario.password,"email":usuario.email,"username":usuario.username,"apellido":usuario.last_name,"nombre":usuario.first_name})
        
    return render (request,"usuario/editar_perfil.html", {"miFormulario":miFormulario,"usuario":usuario})
    
