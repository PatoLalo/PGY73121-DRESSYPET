from django.urls import path
from . import views

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
]
