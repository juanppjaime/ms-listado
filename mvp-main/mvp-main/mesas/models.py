from djongo import models
from pedidos.models import Pedido

class Mesa(models.Model):
    numero = models.IntegerField(primary_key=True)
    pedido = models.EmbeddedField(model_container=Pedido, null=True, blank=True)

    def __str__(self):
        return self.numero
