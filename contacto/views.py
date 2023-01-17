from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .form import FormularioContacto

# Create your views here.

def contacto(request):
    formulario = FormularioContacto()
    
    if request.method == 'POST':
        form = FormularioContacto(data=request.POST)
        
        try:
            if form.is_valid():
                nombre = request.POST.get("nombre")
                email = request.POST.get("email")
                mensaje = request.POST.get("mensaje")
                
                send_mail(
                    "Correo desde Vitrola Web",
                    f"Nombre: {nombre} \nEmail: {email} \n\nMensaje:\n\n {mensaje}",
                    None,
                    ["maximiliano.siracusa@gmail.com"],
                )
                return redirect("/contacto/?ok")
            else:
                return redirect("/contacto/?fail")
        except:
            return redirect("/contacto/?fail")
        
    return render(request,"contacto/contacto.html", {"Formulario":formulario})