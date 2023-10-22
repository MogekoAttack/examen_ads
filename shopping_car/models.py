from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter

# Create your models here.

class ShoppingCar(ClusterableModel):
    STATE_OPTIONS = [
        ("OPEN","Abierto"),
        ("CLOSE","Cerrado"),
    ]
    assigned_user = models.ForeignKey(
        "store_customer.UserStore",
        on_delete=models.CASCADE,
        related_name="user",
        verbose_name="Usuario asignado",
    )
    state = models.CharField(
        max_length=16,
        verbose_name="Estado",
        choices=STATE_OPTIONS,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.assigned_user
    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"

class Sale(ClusterableModel):
    assigned_user = models.ForeignKey(
        "store_customer.UserStore",
        verbose_name="Usuario asignado a carrito",
        on_delete=models.CASCADE,
    )
    assigned_book = models.ForeignKey(
        "catalogo.Book",
        verbose_name="Libro a comprar",
        on_delete=models.CASCADE,
    )
    assigned_car = models.ForeignKey(
        "shopping_car.ShoppingCar",
        verbose_name="Carrito asociado",
        on_delete=models.CASCADE,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.assigned_book
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"