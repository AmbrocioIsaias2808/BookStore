from django import forms

from .models import Libros, Pedidos, Stock

class FCrearPedido(forms.ModelForm):

    class Meta:
        model = Pedidos
        fields = ("Referencia", 'ISBN',"Cantidad","Total","FechaDePedido","Nombre","Email","Telefono","Direccion","CP")

class FSolicitarStock(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ("CantidadInv","ISBN")