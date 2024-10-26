from django.test import TestCase, RequestFactory
from .carrito import Carrito
from .models import Producto  # Make sure Producto model is imported correctly

class CarritoTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        self.request.session = self.client.session  # Attach a session to the request

    def test_carrito_agregar(self):
        carrito = Carrito(self.request)
        print("Carrito instance type:", type(carrito))  # Should print the Carrito class

        # Optionally, test adding a product (requires a product in the database)
        producto = Producto.objects.create(name="Test Product", price=10.0)  # Create a sample product
        carrito.agregar(producto)
        print("Carrito contents:", carrito.carrito)  # Inspect the carrito contents

