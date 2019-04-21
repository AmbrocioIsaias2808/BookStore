from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from django.views.generic import TemplateView
from django.http import request
from .models import Libros,Stock,Pedidos
from .forms import FCrearPedido, FSolicitarStock
import datetime
import random
import time



def search_books(request):
    libros=Libros.objects.all()
    return render(request,"Store/search.html",{"RBusqueda":libros}) #RBusqueda= resultados de busqueda

def CrearPedido(request,ISBN):
    reference = "{}{}{}{}{}{}{}".format(time.strftime("%y"), time.strftime("%S"), time.strftime("%m"),
                                        time.strftime("%M"), time.strftime("%d"), time.strftime("%H"),
                                        str(random.randrange(1000, 9999)))
    inventario = get_object_or_404(Stock, ISBN=ISBN)
    Libro=Libros.objects.get(ISBN=ISBN)
    Stocks=Stock.objects.get(ISBN=ISBN)
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
    return render(request,"Store/Pedidos.html",{"fPedido":form1,"Libro":Libro,"Stock":Stocks,"Inventario":form2,"REFERENCE":reference})


def EditarInformacionPedido(request,Referencia):

    pass


def PagoExitoso(request,referencia,nom):

    pedido=Pedidos.objects.get(Referencia=referencia)
    return render(request, "Store/PagoExitoso.html", {"Pedido": pedido,"Libro":nom})
    pass