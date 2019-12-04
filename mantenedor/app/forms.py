from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    attrs = {
        "type": "password"
    }
    

    class Meta:
        model= Cliente
        fields= ['nombre', 'rut', 'email', 'celular', 'direccion']

