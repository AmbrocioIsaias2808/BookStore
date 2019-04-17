from django.shortcuts import render,redirect
# Create your views here.
from django.views.generic import TemplateView
from django.http import request
from .models import Libros,Stock,Pedidos

def search_books(request):
    libros=Libros.objects.all()
    return render(request,"Store/search.html",{"RBusqueda":libros}) #RBusqueda= resultados de busqueda

def specific_book(request):

    pass


