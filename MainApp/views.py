from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import Formulario
from .carrito import Carrito
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login


# Create your views here.

def Tienda(request):
    return render(request, 'Tienda Verde.html')

def Productos(request):

    Productos = Producto.objects.all()
    return render(request, 'Productos.html', {
        'productos' : Productos
    })

def Login(request):
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            print(f"Attempting login with email: {email} and password: {password}")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = Formulario()
    
    return render(request, 'login.html', {
        'form': form
        })

def Register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
        else:
            data['form'] = user_creation_form

    return render(request, 'register.html', data)

def exit(request):
    logout(request)
    return redirect('/')

def Carrito_view(request):
    productos = Producto.objects.all()
    return render(request, 'carrito.html', {
        'productos':productos,
    })

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    print("Carrito instance type:", type(carrito))
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("/carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("/carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("/carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("/productos")


def crear_pedido_view(request):
    carrito = Carrito(request)
    pedido = carrito.crear_pedido()
    carrito.limpiar()
    return redirect('/carrito')


