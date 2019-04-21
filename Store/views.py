from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from django.views.generic import TemplateView
from django.http import request
from django.http import HttpResponse
from .models import Libros,Stock,Pedidos
from .forms import FCrearPedido, FSolicitarStock
import datetime
import random
import time
from django.views.generic import TemplateView



def search_books(request):
    libros=Libros.objects.all()
    return render(request,"Store/search.html",{"RBusqueda":libros}) #RBusqueda= resultados de busqueda

class BarraDeBusqueda(TemplateView):
    def post(self,request):
        search = request.POST["search"]
        Datos = Libros.objects.filter(Titulo__contains=search)
        if is_empty(Datos) == 1:
            Datos = Libros.objects.filter(Autor__contains=search)
            if is_empty(Datos) == 1:
                Datos = Libros.objects.filter(Editorial__contains=search)
                if is_empty(Datos)==1:
                    Datos=Libros.objects.filter(Descripcion__contains=search)
        return render(request, "Store/search.html", {"RBusqueda": Datos})  # RBusqueda= resultados de busqueda


def is_empty(data_structure):
    if data_structure:
        return 0
    else:
        return 1

def CrearPedido(request,ISBN):
    reference = "{}{}{}{}{}{}{}".format(time.strftime("%y"), time.strftime("%S"), time.strftime("%m"),
                                        time.strftime("%M"), time.strftime("%d"), time.strftime("%H"),
                                        str(random.randrange(1000, 9999)))
    try:
        #inventario = get_object_or_404(Stock, ISBN=ISBN)
        inventario =Stock.objects.get(ISBN=ISBN)
        Libro=Libros.objects.get(ISBN=ISBN)
        if request.method == "POST":
            form1 = FCrearPedido(request.POST)
            form2=FSolicitarStock(request.POST,instance=inventario)
            if form1.is_valid() and form2.is_valid():
                referencia = request.POST.get('Referencia')
                print("Referencia:",referencia," ISBN: ",ISBN)
                inventario=form2.save(commit=False)
                post = form1.save(commit=False)
                post.save()
                inventario.save()
                InformacionDelPedido=Pedidos.objects.get(Referencia=referencia)
                return render(request,"Store/Pagos.html",{"Pedido":InformacionDelPedido,"Libro":Libro})

        else:
            form1 = FCrearPedido()
            form2=FSolicitarStock(instance=inventario)
        return render(request,"Store/Pedidos.html",{"fPedido":form1,"Libro":Libro,"Stock":inventario,"Inventario":form2,"REFERENCE":reference})
    except:
        return faltadestock(request)


def faltadestock(request):
    return render(request,"Store/SinStock.html")


def PagoExitoso(request,referencia,nom):

    pedido=Pedidos.objects.get(Referencia=referencia)
    return render(request, "Store/PagoExitoso.html", {"Pedido": pedido,"Libro":nom})
    pass