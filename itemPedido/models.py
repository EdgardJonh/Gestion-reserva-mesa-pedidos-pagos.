from django.db import models
from pedido.models import Pedido
from producto.models import Producto
# Create your models here.
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Item {self.producto.nombre} x {self.cantidad} - Pedido {self.pedido.id}'