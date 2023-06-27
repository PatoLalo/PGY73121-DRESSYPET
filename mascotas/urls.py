from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('reservas', views.reservas, name="reservas"),
    path('trabajo', views.trabajo, name="trabajo"),
    path('contacto', views.contacto, name="contacto"),
    path('tipo_servicio', views.tipo_servicio, name="tipo_servicio"),
    
]
