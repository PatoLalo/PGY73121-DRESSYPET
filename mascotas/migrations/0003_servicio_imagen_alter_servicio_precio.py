# Generated by Django 4.1.2 on 2023-07-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_reserva_servicios_servicio_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='servicios/'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(null=True),
        ),
    ]
