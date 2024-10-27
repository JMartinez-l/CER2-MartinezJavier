from django.db import models

# Create your models here.

class Producto(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=200)
    imagen = models.ImageField(
        upload_to="productos",
        null=True
    )

    def __str__(self):
        return f'{self.name} -> {self.price}'
    
class Pedidos(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    partialPrice = models.IntegerField()
    Estados = (
        ('P', 'Pendiente'),
        ('C', 'Completado')
    )
    estate = models.CharField(max_length=1, choices=Estados, default='C')
