from django.shortcuts import render

from mascotas.models import Reserva, Servicio
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    
    request.session["usuario"]="Phurtado"
    usuario=request.session["usuario"]
    context={"usuario":usuario}
    return render(request,'mascotas/index.html', context)

def index(request):
    context={}
    return render(request, 'mascotas/index.html', context)

def carritoAdm(request):
    servicios= Servicio.objects.all()
    context={'servicios': servicios}
    return render(request, 'mascotas/carritoAdm.html', context)

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

def servicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'mascotas/servicios.html', context)

def carrito(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request, 'mascotas/carrito.html', context)

def registrar_reserva(request):
    if request.method == 'POST':
        
        nombre_cliente = request.POST.get('nombre_cliente')
        nombre_mascota = request.POST.get('nombre_mascota')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        raza = request.POST.get('raza')
        
        
      
        reserva = Reserva.objects.create(
                                        nombre_cliente=nombre_cliente,
                                        nombre_mascota=nombre_mascota,
                                        email=email,
                                        telefono=telefono,
                                        fecha_reserva=fecha,
                                        hora_reserva=hora,
                                        raza=raza,)
                                        
        reserva.save()
        
        servicios = Servicio.objects.all()
     
        return render(request,'mascotas/carrito.html', {'reserva': reserva, 'servicios':servicios})
    return render(request, 'mascotas/reservas.html')


