from django.shortcuts import redirect, render

from mascotas.models import Reserva, Servicio

# Create your views here.


def index(request):
    context={}
    return render(request,'mascotas/index.html', context)

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

def carrito(request):
    context={}
    return render(request, 'mascotas/carrito.html', context)

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
        return render(request,'mascotas/carrito.html', {'reserva': reserva})

    # Si no es una solicitud POST, renderiza el formulario nuevamente o realiza cualquier otra acción que desees
    return render(request, 'mascotas/reservas.html')

def busqueda(request):
    if request.method == 'GET':
        cliente = request.GET.get('cliente')  # Obtener el nombre del cliente desde la solicitud GET

        # Realizar la búsqueda en la base de datos
        if cliente:
            reservas = None
            reservas = Reserva.objects.filter(nombre_cliente__icontains=cliente)
        else:
            reservas = None
        # Renderizar el resultado de la búsqueda en un template
        return render(request, 'mascotas/carrito.html', {'reservas': reservas})

    return render(request, 'mascotas/carrito.html')