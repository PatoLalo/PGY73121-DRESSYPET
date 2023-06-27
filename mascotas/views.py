from django.shortcuts import render

from .models import Servicio

# Create your views here.
def index(request):
    context={}
    return render(request, 'mascotas/index.html', context)

def nosotros(request):
    context={}
    return render(request, 'mascotas/nosotros.html', context)

def reservas(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'mascotas/reservas.html', context)

def trabajo(request):
    context={}
    return render(request, 'mascotas/trabajo.html', context)

def contacto(request):
    context={}
    return render(request, 'mascotas/contacto.html', context)

def tipo_servicio(request):
    servicios = Servicio.objects.all()
    context= {"servicios": servicios}
    return render(request, 'mascotas/reservas.html', context)