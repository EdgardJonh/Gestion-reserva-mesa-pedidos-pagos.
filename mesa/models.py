from django.db import models

# Create your models here.
class Mesa(models.Model):
    capacidad = models.IntegerField(unique=True)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f'Mesa {self.capacidad} - {self.ubicacion}'