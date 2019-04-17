from django.contrib import admin
from .models import Libros,Pedidos,Stock
# Register your models here.
admin.site.register(Libros)
admin.site.register(Stock)
admin.site.register(Pedidos)