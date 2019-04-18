from django.db import models
import datetime
import random
import time
from django.utils import timezone

class Libros(models.Model):
    ISBN = models.CharField(max_length=20, primary_key=True, verbose_name="ISBN ", db_column="ISBN")
    Titulo=models.CharField(max_length=50,verbose_name="Titulo del Libro", db_column="Titulo")
    Autor=models.CharField(max_length=50, verbose_name="Autor ", db_column="Autor")
    genero=(("1","Accion"),("2","Aventura"),("3","Terror"),("4","Fantasia"),("5","Ciencia Ficcion"),("6","No ficcion/Realidad"),("7","Investigacion"),("8","Biografica"),("9","Infantil"),("10","Autoayuda"),("11","Eroticos/Adultos"),("12","Hogar"),("13","Cocina"),("14","Enciclopedia/Manual"),("15","Politica"),("16","Economia/Marketing"),("17","Socioedad"),("18","Viajes/Cultura"),("19","Historicos"),("20","Clasicos"),("21", "Espiritual"),("22", "Poesia"),("23", "Suspenso"),("24", "Otros Temas/ Varios"),)
    Genero=models.CharField(choices=genero, default="1", verbose_name="Genero: ", db_column="Genero", max_length=2)
    Editorial=models.CharField(max_length=50,verbose_name="Editorial ", db_column="Editorial")
    Publicacion=models.DateField(verbose_name="Fecha de Publicacion ", db_column="Publicacion")
    Edicion=models.CharField(max_length=50, verbose_name="Edicion ", db_column="Edicion")
    Descripcion=models.TextField(max_length=500,verbose_name="Descripcion",db_column="Descripcion",blank=True)
    Precio=models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Precio ", db_column="Precio")
    Portada=models.ImageField(upload_to="Portadas",verbose_name="Portada del Libro ",db_column="Portada",blank=True, null=True)

    def alta(self):
        self.save()

    def __unicode__(self):
        return str(self.Portada)

    def __str__(self):
        return "{} : {} : {}".format(self.ISBN,self.Titulo,self.Autor)

    class Meta:
        db_table = "Libros"

class Stock(models.Model):
    ISBN=models.ForeignKey("Libros",verbose_name="ISBN ",db_column="ISBN",on_delete=models.CASCADE, primary_key=True)
    CantidadInv=models.IntegerField(verbose_name="Cantidad", db_column="Cantidad", default=0)

    def alta(self):
        self.save()

    def __str__(self):
        return "{} : {}".format(self.ISBN,self.CantidadInv)

    class Meta:
        db_table = "Stock"

class Pedidos(models.Model):
    reference = "{}{}{}{}{}{}{}".format(time.strftime("%y"), time.strftime("%S"), time.strftime("%m"),
                                      time.strftime("%M"), time.strftime("%d"), time.strftime("%H"),
                                      str(random.randrange(1000, 9999)))
    Referencia=models.CharField(null=False,max_length=16,verbose_name="Referencia ", db_column="Referencia",primary_key=True,default=reference)
    ISBN=models.ForeignKey("Libros",db_column="ISBN",verbose_name="ISBN", on_delete=models.CASCADE)
    Cantidad=models.IntegerField(default=0, verbose_name="Cantidad ", db_column="Cantidad")
    Total=models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Total: ", db_column="Total")
    FechaDePedido=models.DateField(default=timezone.now(), verbose_name="Fecha De Pedido")
    Nombre=models.CharField(max_length=50, verbose_name="Nombre ", db_column="Cliente")
    Email=models.EmailField(verbose_name="Correo Electronico ", db_column="Email")
    Direccion=models.CharField(max_length=100,verbose_name="Direccion ", db_column="Direccion")
    CP=models.IntegerField(verbose_name="Codigo Postal", db_column="CP")
    status=(("VP","Verificando Pago"),("PV","Pago Verificado"),("PE","En Proceso de Envio"),("E","Enviado"),("R","Recibido"))
    Estatus=models.CharField(choices=status, default="VP", verbose_name="Estatus ", db_column="Estatus", max_length=2)


    def alta(self):
        self.save()

    def __str__(self):
        return "{} : {}".format(self.Referencia,self.Estatus)

    class Meta:
        db_table = "Pedidos"

