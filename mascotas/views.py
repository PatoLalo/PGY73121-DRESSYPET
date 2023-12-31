from django.shortcuts import redirect, render
from mascotas.forms import AgregarServicioForm, ServicioForm

from mascotas.models import Reserva, Servicio
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm
from django.contrib.auth.models import User

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


def eliminar_servicio(request, pk):
    context={}
    try:
        servicio = Servicio.objects.get(id_servicio=pk)
        servicio.delete()
        
        mensaje="Bien, datos eliminados..."
        servicios = Servicio.objects.all()
        context = {'servicios': servicios, 'mensaje': mensaje}
        return render(request,'mascotas/carritoAdm.html', context)
    except:
        mensaje="Error, no existe..."
        servicios = Servicio.objects.all()
        context = {'servicios': servicios, 'mensaje': mensaje}
        
def modificar_servicio(request, pk):
    servicio = Servicio.objects.get(id_servicio=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('carritoAdm')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'mascotas/modificar_servicio.html', {'form': form, 'servicio': servicio})

def agregar_servicio(request):
    if request.method == 'POST':
        form = AgregarServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('carritoAdm')  # Redirige a la vista carritoAdm.html
    else:
        form = AgregarServicioForm()

    return render(request, 'mascotas/agregar_servicio.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            nombre_cliente = form.cleaned_data['nombre_cliente']
            apellido = form.cleaned_data['apellido']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username=username, password=password)
            user.nombre_cliente = nombre_cliente
            user.apellido = apellido
            user.email = email
            user.telefono = telefono
            user.save()

            login(request, user)

            return redirect('index')
    else:
        form = CustomRegistrationForm()

    return render(request, 'mascotas/registro.html', {'form': form})
