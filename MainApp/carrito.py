from .models import Pedidos


class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.name,
                "acumulado": producto.price,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.price
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.price
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def crear_pedido(self):
        # You can adjust the fields as necessary
        total_price = sum(item['acumulado'] for item in self.carrito.values())
        
        user_email = self.request.user.email

        description_lines = []
        for item in self.carrito.values():
            line = f"{item['nombre']} - Cantidad: {item['cantidad']}, Total: {item['acumulado']}"
            description_lines.append(line)
            description = "\n".join(description_lines)
                            
        # Create a new Pedido
        pedidos = Pedidos.objects.create(
            name="Pedido from " + user_email,
            description=description,
            partialPrice=total_price,
            estate='P' 
        )

        return pedidos

        