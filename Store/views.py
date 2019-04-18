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
    if request.method == "POST":
        form1 = FCrearPedido(request.POST)
        form2=FSolicitarStock(request.POST,instance=inventario)
        if form1.is_valid() and form2.is_valid():
            inventario=form2.save(commit=False)
            post = form1.save(commit=False)
            post.save()
            inventario.save()
            return redirect('/')

    else:
        form1 = FCrearPedido()
        form2=FSolicitarStock(instance=inventario)
    Libro=Libros.objects.get(ISBN=ISBN)
    Stocks=Stock.objects.get(ISBN=ISBN)
    redirect('/')
    return render(request,"Store/Pedido.html",{"fPedido":form1,"Libro":Libro,"Stock":Stocks,"Inventario":form2,"REFERENCE":reference})


