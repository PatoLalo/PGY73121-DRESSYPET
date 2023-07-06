import datetime
from django.db import models
from django.forms import ValidationError

# Create your models here.

class Servicio(models.Model):
    id_servicio  = models.AutoField(db_column='idServicio', primary_key=True) 
    servicio     = models.CharField(max_length=50, blank=False, null=False)
    precio       = models.IntegerField( null=True)
    imagen       = models.ImageField(upload_to='servicios/', default='default.jpg')

    def formato_precio(self):
        return "{:,}".format(self.precio).replace(",", ".")

    def __str__(self):
        return str(self.servicio)
    
    
class Reserva(models.Model):
    nombre_cliente   = models.CharField(primary_key=True, max_length=10)
    nombre_mascota   = models.CharField(max_length=20)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True) 
    telefono         = models.CharField(max_length=45)
    fecha_reserva    = models.DateField()
    hora_reserva     = models.TimeField()
    raza             = models.CharField(max_length=50) 
    servicios        = models.ManyToManyField(Servicio)

    def clean(self):
        if self.hora_reserva and self.hora_reserva.hour < 9 or self.hora_reserva.hour > 19:
            raise ValidationError("La hora de reserva debe estar entre las 9 AM y las 7 PM.")

        if self.fecha_reserva and self.fecha_reserva < datetime.date.today():
            raise ValidationError("La fecha de reserva no puede ser en el pasado.")