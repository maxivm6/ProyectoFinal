from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="",max_length=20,required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    email = forms.EmailField(label="",required=True)
    mensaje = forms.CharField(label="",max_length=500,required=True,widget=forms.Textarea(attrs={'placeholder': 'Mensaje'}))
    
    def __init__(self, *args, **kwargs):
        super(FormularioContacto, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'