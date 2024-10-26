from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tienda),
    path('productos/', views.Productos),
    path('login/', views.Login),
    path('register/', views.Register),
    path('logout/' , views.exit),
    path('carrito/', views.Carrito_view),
]




