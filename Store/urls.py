from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.search_books,name="search"),
    path('CrearPedido/<ISBN>/', views.CrearPedido, name='CrearPedido'),
]