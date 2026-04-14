from django.db import models

class Organizacion(models.Model):
    TIPOS = [
        ('Fundacion', 'Fundacion'),
        ('Junta', 'Junta de Vecinos'),
        ('Club', 'Club Deportivo'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    direccion = models.CharField(max_length=200)
    contacto = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
# Create your models here.
