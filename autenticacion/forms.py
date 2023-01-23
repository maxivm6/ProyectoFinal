from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.core.exceptions import ValidationError  
        
class CustomForm(UserCreationForm):  
    username = forms.CharField(label=' ', min_length=5, max_length=150, widget= forms.TextInput (attrs= {'placeholder': 'Nombre de usuario',}))  
    email = forms.EmailField(label=' ', widget= forms.EmailInput (attrs= {'placeholder': 'Dirección de email'}))  
    password1 = forms.CharField(label=' ', widget=forms.PasswordInput (attrs= {'placeholder': 'Contraseña',}))  
    password2 = forms.CharField(label=' ', widget=forms.PasswordInput (attrs= {'placeholder': 'Repita su contraseña',}))  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("Usuario ya existente")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Email ya existente")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas no coinciden")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']  
        )  
        return user 

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='\n', min_length=5, max_length=150, widget= forms.TextInput (attrs= {'placeholder': 'Nombre de usuario',}))
    password = forms.CharField(label='\n', widget=forms.PasswordInput (attrs= {'placeholder': 'Contraseña',}))    