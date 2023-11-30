from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter

class Libro(models.Model):
    nombre = models.CharField(
        max_length=32,
        default="",
        verbose_name="Nombre del libro",
    )
    isbn = models.CharField(
        max_length=32,
        default="",
        verbose_name="ISBN",
    )
    precio = models.IntegerField(
        default=0,
        verbose_name="Precio",
    )
    cantidad = models.IntegerField(
        default=0,
        verbose_name="Cantidad",
    )
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Lista de libros"

class Carrito(models.Model):
    libro_comprado = models.ForeignKey(
        "liberria.Libro",
        verbose_name="Libro comprado",
        on_delete=models.CASCADE,
    )
    cantidad = models.IntegerField(
        default=0,
        verbose_name="Cantidad",
    )
    def __str__(self):
        return "Carrito: "+str(self.pk)
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Lista de compras"

class Cliente(models.Model):
    nombre = models.CharField(
        max_length=32,
        default="",
        verbose_name="Nombre completo",
    )
    tarjeta = models.CharField(
        max_length=32,
        default="",
        verbose_name="Número de tarjeta",
    )
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Lista de clientes"

class Ticket(models.Model):
    nombre_comprador = models.ForeignKey(
        "liberria.Cliente",
        verbose_name="Comprador",
        on_delete=models.CASCADE,
    )
    tarjeta = models.CharField(
        max_length=32,
        verbose_name="Tarjeta",
        default="1234 1234 1234 1234"
    )
    compras = models.CharField(
        max_length=512,
        verbose_name="Compras",
    )
    def __str__(self):
        return "Ticket: " + str(self.pk)
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Lista de tickets"