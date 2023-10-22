from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.api.v2.filters import OrderingFilter, FieldsFilter
# Create your models here.

class Author(ClusterableModel):
    name = models.CharField(
        verbose_name="Nombre del autor",
        max_length=32,
    )
    registration_year = models.DateField(
        verbose_name="Fecha de registro",
    )
    birthdate = models.DateField(
        verbose_name="Fecha de nacimiento",
    )
    gender = models.ForeignKey(
        "catalogo.Gender",
        verbose_name="Género",
        on_delete=models.CASCADE,
    )
    languaje = models.ForeignKey(
        "catalogo.Languaje",
        verbose_name="Idioma principal",
        on_delete=models.CASCADE,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Editorial(ClusterableModel):
    OPTIONS_FORMAT = [
        ("HARD","Pasta dura"),
        ("SOFT","Pasta suave"),
        ("DIGITAL","Digital"),
        ("SOUND","Audio libros"),
        ("UNKNOW","Desconocido"),
    ]
    name = models.CharField(
        verbose_name="Nombre de la editorial",
        max_length=32,
    )
    registration_year = models.DateField(
        verbose_name="Fecha de registro",
    )
    format = models.CharField(
        verbose_name="Formato de públicación",
        max_length=16,
        choices=OPTIONS_FORMAT,
    )
    gender = models.ForeignKey(
        "catalogo.Gender",
        verbose_name="Género",
        on_delete=models.CASCADE,
    )
    languaje = models.ForeignKey(
        "catalogo.Languaje",
        verbose_name="Idioma principal",
        on_delete=models.CASCADE,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"

class Book(ClusterableModel):
    name = models.CharField(
        verbose_name="Nombre del libro",
        max_length=32,
    )
    edition = models.IntegerField(
        verbose_name="Edición",
    )
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=32,
    )
    publication_date = models.DateField(
        verbose_name="Fecha de publicación (Se ignorará el día)",
    )
    gender = models.ForeignKey(
        "catalogo.Gender",
        verbose_name="Género",
        on_delete=models.CASCADE,
    )
    languaje = models.ForeignKey(
        "catalogo.Languaje",
        verbose_name="Idioma principal",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        "catalogo.Author",
        verbose_name="Autor",
        on_delete=models.CASCADE,
        default=1,
    )
    editorial = models.ForeignKey(
        "catalogo.Editorial",
        verbose_name="Editorial",
        on_delete=models.CASCADE,
    )
    number_of_books = models.IntegerField(
        default=1,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

class Gender(ClusterableModel):
    name = models.CharField(
        max_length=32,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

class Languaje(ClusterableModel):
    name = models.CharField(
        max_length=32,
    )
    filter_backends = [
        FieldsFilter,
        OrderingFilter
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"