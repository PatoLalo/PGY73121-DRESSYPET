from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('index', views.index, name="index"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('reservas', views.reservas, name="reservas"),
    path('trabajo', views.trabajo, name="trabajo"),
    path('contacto', views.contacto, name="contacto"),
    path('carrito', views.carrito, name="carrito"),
    path('carritoAdm', views.carritoAdm, name="carritoAdm"),
    path('servicios', views.servicios, name="servicios"),
    path('registrar_reserva', views.registrar_reserva, name="registrar_reserva"),
    
    path('eliminar_servicio/<str:pk>', views.eliminar_servicio, name='eliminar_servicio'),
    path('modificar_servicio/<str:pk>', views.modificar_servicio, name='modificar_servicio'),
    path('agregar_servicio', views.agregar_servicio, name="agregar_servicio"),
    path('register', views.register, name='register'),
]
