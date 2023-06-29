from django.shortcuts import redirect, render

from .models import Reserva, Servicio

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

def registrar_reserva(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_cliente = request.POST.get('nombre_cliente')
        nombre_mascota = request.POST.get('nombre_mascota')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        raza = request.POST.get('raza')
        
        # Guardar los datos en tu modelo Reserva o realizar cualquier otra acción que desees
        reserva = Reserva.objects.create(
                                        nombre_cliente=nombre_cliente,
                                        nombre_mascota=nombre_mascota,
                                        email=email,
                                        telefono=telefono,
                                        fecha_reserva=fecha,
                                        hora_reserva=hora,
                                        raza=raza,)
        reserva.save()
        # Redirigir a una página de éxito o realizar cualquier otra acción que desees
        return redirect('mascotas/contacto.html')

    # Si no es una solicitud POST, renderiza el formulario nuevamente o realiza cualquier otra acción que desees
    return render(request, 'mascotas/reservas.html')