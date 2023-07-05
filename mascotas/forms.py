from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['servicio', 'precio']
        
class AgregarServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['servicio', 'precio']