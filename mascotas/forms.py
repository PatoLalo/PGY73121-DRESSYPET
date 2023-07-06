from django import forms
from .models import Servicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['servicio', 'precio']
        
class AgregarServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['servicio', 'precio', 'imagen']
        

class CustomRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150, min_length=2)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=8)
    password_confirmation = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, min_length=8)
    nombre_cliente = forms.CharField(label='Nombre', max_length=30, min_length=2)
    apellido = forms.CharField(label='Apellido', max_length=30, min_length=2)
    telefono = forms.CharField(label='Número de teléfono', max_length=15)
    email = forms.EmailField(label='Correo electrónico')


class Meta:
    model = User
    fields = ['username', 'password', 'password_confirmation', 'nombre_cliente', 'apellido', 'telefono', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nombre_cliente = self.cleaned_data['nombre_cliente']
        user.apellido = self.cleaned_data['apellido']
        user.email = self.cleaned_data['email']
        user.telefono = self.cleaned_data['telefono']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user