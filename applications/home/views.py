# La vistas genericas son vistas que hacen una tarea predefinida y ya, ya sea crear, mostrar o eliminar objetos,
# por ejemplo.

from django.views.generic import TemplateView, ListView, CreateView

# importando el/los modelos que se usaran

from .models import Prueba
from .form import PruebaModels


# Create your views here.

# una template view es una vista generica que solo se encarga de mostrar una template HTML

class Test(TemplateView):
    # template_name recibe el nombre de la pagina html que usaremos como template.
    template_name = "home/prueba.html"


class resumeFound(TemplateView):
    # template_name recibe el nombre de la pagina html que usaremos como template.
    template_name = "home/resumeFound.html"


# una listview es una vista generica que se encarga de mostrar multiples instancias de una tabla de una base de datos
# recibe una template html (template_name y un modelo (base de datos)

class Lista(ListView):

    template_name = "home/lista.html"

    # context_object_name creara una "variable" la cual guardara el valor del objeto en contexto, en este caso la lista
    # de numeros que creamos.

    context_object_name = "ListaNumeros"

    # queryset sirve para mostrar una lista de elementos, en este caso reemplazando a la base de datos

    queryset = ["1", "10", "50", "25"]


# Una vez se crea una vista nueva, la misma debe agregarse al archivo urls

class ListPrueba(ListView):

    template_name = "home/listarPrueba.html"

    # De esta manera se asigna un modelo a una vista

    model = Prueba
    context_object_name = "list"

# Una createview se encarga de insertar registros dentro de nuestra base de datos, recibe los siguientes atributos
# una template donde se desplegara, un modelo y los campos de dicho modelo los cuales queramos trabajar

class CreatePrueba(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaModels
    success_url = "/"
