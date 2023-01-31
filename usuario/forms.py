from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class UserEditForm(UserCreationForm):
    apellido = forms.CharField(label="Apellido/s", required=False)
    nombre = forms.CharField(label="Nombre/s", required=False)
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField(label='Email', required=True)
   
    password1 = forms.CharField(label='Nueva contraseña',widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Nueva contraseña (confirmación)',widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = User
        fields = ['username','email', 'nombre','apellido','password1','password2']
    
