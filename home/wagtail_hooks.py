from wagtail.snippets.views.snippets import SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from catalogo.models import (
    Author,
    Editorial,
    Book,
)

from store_customer.models import (
    UserStore,
)

from shopping_car.models import (
    Sale,
    ShoppingCar,
)
#Buttons from catalogos
class AuthorMenu(SnippetViewSet):
    model = Author
    menu_label = "Autores"

class EditorialMenu(SnippetViewSet):
    model = Editorial
    menu_label = "Editoriales"

class BookMenu(SnippetViewSet):
    model = Book
    menu_label = "Libros"
#Buttons from sales
class UserStoreMenu(SnippetViewSet):
    model = UserStore
    menu_label = "Usuarios de tienda"

class SaleMenu(SnippetViewSet):
    model = Sale
    menu_label = "Todas las ventas"

class ShoppingCarMenu(SnippetViewSet):
    model = ShoppingCar
    menu_label = "Carritos de venta"

#Buttons from groups
class AllSalesMenu(SnippetViewSetGroup):
    menu_label = "Ventas"
    items = [
        UserStoreMenu,
        SaleMenu,
        ShoppingCarMenu,
    ]

class CatalogoMenu(SnippetViewSetGroup):
    menu_label = "Catalogo"
    items = [
        AuthorMenu,
        EditorialMenu,
        BookMenu,
    ]

register_snippet(CatalogoMenu)
register_snippet(AllSalesMenu)