from wagtail.snippets.views.snippets import SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from liberria.models import (
    Libro,
    Cliente,
    Carrito,
    Ticket,
)

class LibroMenu(SnippetViewSet):
    model = Libro
    menu_label = "Libros"

class ClienteMenu(SnippetViewSet):
    model = Cliente
    menu_label = "Clientes"

class CarritoMenu(SnippetViewSet):
    model = Carrito
    menu_label = "Carrito"

class TicketMenu(SnippetViewSet):
    model = Ticket
    menu_label = "Tickets"

class LibreriaRegistro(SnippetViewSetGroup):
    menu_label = "Libreria"
    items = [
        LibroMenu,
        ClienteMenu,
        CarritoMenu,
        TicketMenu,
    ]

register_snippet(LibreriaRegistro)