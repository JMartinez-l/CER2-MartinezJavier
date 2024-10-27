from django.contrib import admin
from .models import Producto, Pedidos

# Register your models here.

admin.site.register(Producto)

@admin.register(Pedidos)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['name', 'partialPrice', 'estate'] 

