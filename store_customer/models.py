from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter

# Create your models here.

class UserStore(ClusterableModel):
    name = models.CharField(
        verbose_name="Nombre(s)",
        max_length=32,
    )
    first_last_name = models.CharField(
        verbose_name="Apellido paterno",
        max_length=32,
    )
    second_last_name = models.CharField(
        verbose_name="Apellido materno",
        max_length=32,
    )
    assigned_car = models.ForeignKey(
        "shopping_car.ShoppingCar",
        verbose_name="Carrito asignado",
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"