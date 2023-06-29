from django import forms
from .models import Servicio

from django.forms import ModelForm

class ReservaForm(forms.Form):
    nombre_cliente = forms.CharField(label='Nombre cliente')
    nombre_mascota = forms.CharField(label='Nombre mascota')
    tipo_servicio = forms.ModelChoiceField(queryset=Servicio.objects.all(), label='Tipo de servicio')
    email = forms.EmailField(label='Email')
    telefono = forms.CharField(label='Teléfono')
    fecha = forms.DateField(label='Fecha para reservar')
    hora = forms.ChoiceField(label='Hora de reserva')
    raza = forms.CharField(label='Raza')