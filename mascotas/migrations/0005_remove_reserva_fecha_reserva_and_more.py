# Generated by Django 4.2.3 on 2023-07-06 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='fecha_reserva',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='hora_reserva',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='nombre_mascota',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='raza',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='servicios',
        ),
    ]
