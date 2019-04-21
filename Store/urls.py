from django.contrib import admin
from django.urls import path, include
from . import views
from .views import BarraDeBusqueda

urlpatterns = [
    path("",views.search_books,name="Index"),
    path("resultados",BarraDeBusqueda.as_view(),name="search"),
    path('CrearPedido/<ISBN>/', views.CrearPedido, name='CrearPedido'),
    path('Pago_Exitoso/REF=<referencia>/<nom>/', views.PagoExitoso, name='CrearPedido'),
    path('Falta_De_Stock',views.faltadestock, name="faltadestock")
]