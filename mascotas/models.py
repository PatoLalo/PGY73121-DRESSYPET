import datetime
from django.db import models
from django.forms import ValidationError

# Create your models here.

class Servicio(models.Model):
    id_servicio  = models.AutoField(db_column='idServicio', primary_key=True) 
    servicio     = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return str(self.servicio)
    
    
class Reserva(models.Model):
    nombre_cliente   = models.CharField(primary_key=True, max_length=10)
    nombre_mascota   = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20) 
    id_Servicio      = models.ForeignKey('Servicio',on_delete=models.CASCADE, db_column='idServicio')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    hora_reserva     = models.TimeField()
    fecha_reserva    = models.DateField() 

    def clean(self):
        if self.hora_reserva and self.hora_reserva.hour < 9 or self.hora_reserva.hour > 19:
            raise ValidationError("La hora de reserva debe estar entre las 9 AM y las 7 PM.")

        if self.fecha_reserva and self.fecha_reserva < datetime.date.today():
            raise ValidationError("La fecha de reserva no puede ser en el pasado.")

