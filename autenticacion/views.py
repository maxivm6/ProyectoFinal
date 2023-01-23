from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CustomForm, CustomLoginForm
from django.contrib.auth import login , logout, authenticate
from django.contrib import messages

def loguear(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=name,password=contra)
            if usuario is not None:
                login(request,usuario)
                return redirect('index')
            else:
                messages.error(request,"usuario y/o contraseña incorrectos")
        else:
            messages.error(request,"usuario y/o contraseña incorrectos")
    
    form = CustomLoginForm()
    return render(request,"autenticacion/login.html",{'form':form})


class Registro(View):
    
    def get(self,request):
        form = CustomForm ()
        return render(request,'autenticacion/registro.html',{'form':form})
    
    def post(self,request):
        form = CustomForm (request.POST)
        
        if form.is_valid():
            usuario = form.save()
        
            login (request,usuario)
            
            return redirect('index')
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
                return render(request,'autenticacion/registro.html',{'form':form})
        
def cerrar_sesion(request):
    logout(request)
    
    return redirect('index')