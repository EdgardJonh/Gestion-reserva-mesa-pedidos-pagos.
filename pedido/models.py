from django.db import models
from reserva.models import Reserva
from cliente.models import Cliente
from metodoPago.models import MetodoPago
# Create your models here.
class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('procesado', 'Procesado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True, related_name="pedidos")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f'Pedido {self.id} - {self.cliente}'