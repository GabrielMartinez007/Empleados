from django.shortcuts import render
from django.views.generic import ListView, \
    DetailView, \
    CreateView, \
    TemplateView, \
    UpdateView, \
    DeleteView

from django.urls import reverse_lazy

from .models import Empleado


# Create your views here.


class ListAll(ListView):
    template_name = "persona/ListAll.html"
    paginate_by = 4
    ordering = "first_Name"
    model = Empleado


class ListByArea(ListView):
    template_name = "persona/ListBy.html"

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            department__short_name=area
        )

        return lista


class ListbyKey(ListView):
    template_name = "persona/ListByKey.html"
    context_object_name = "empleado"

    def get_queryset(self):
        # en palabra_clave se almacenan los datos que fueron interceptados del GET, en este caso mediante el id de uno
        # de ellos "kword" estoy interceptando los datos del input.

        palabra_clave = self.request.GET.get("kword", " ")
        lista = Empleado.objects.filter(
            first_Name=palabra_clave
        )

        return lista


class BuscarHabsEmpleado(ListView):
    template_name = "persona/BuscarHabsEmpleado.html"
    context_object_name = "Habs"

    def get_queryset(self):
        ide = self.request.GET.get("habilidad", "")
        print(ide)
        empleado = Empleado.objects.get(id=ide)
        return empleado.Habilidades.all()


class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = "persona/detailEmpleado.html"

    # el get context datan es donde se guarda la variablo de la vista.
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetail, self).get_context_data(**kwargs)
        cont = super(EmpleadoDetail, self).get_context_data(**kwargs)

        # proceso, codigo y etc

        # para asignar un valor a dicho contexto solo hay que hacer la siguiente instruccion y declarar el valor
        context['titulo'] = "Empleado del mes"
        return context


class Success(TemplateView):
    template_name = "persona/success.html"


class Add(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = [
        "first_Name",
        "last_Name",
        "job",
        "department",
        "Habilidades",
    ]
    success_url = reverse_lazy("persona_app:correcto")

    # La funcion form_valid es la que se encarga de guardar los datos una vez son validos en la bbdd
    # los mismos se pueden interceptar en caso de ser requerido, como es en este caso con full_name
    def form_valid(self, form):
        # logica
        # aqui estoy creando una instancia del propio modelo de la base de datos llamada empleados
        empleado = form.save(commit=False)
        # se puede llamar a cualquiera de los atributos del modelo mediante la regla del "." y jugar con ellos.
        empleado.full_Name = empleado.first_Name + " " + empleado.last_Name
        # aqui estoy guardando los cambios que hice dentro de la base de datos
        empleado.save()
        # retorno de los datos.
        return super(Add, self).form_valid(form)

class UpdateEmpleado(UpdateView):
    model = Empleado
    template_name = "persona/UpdateEmpleado.html"
    fields = fields = [
        "first_Name",
        "last_Name",
        "job",
        "department",
        "Habilidades",
    ]
    success_url = reverse_lazy("persona_app:correcto")

    # A travez de interceptar el metodo post puedo crear sistemas y logicas con la informacion que el navegador
    # envia al servidor.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #logica.....
        print("metodo post **************************")
        print(request.POST)
        print(request.POST["first_Name"])
        #logica......
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # logica
        # aqui estoy creando una instancia del propio modelo de la base de datos llamada empleados
        # se puede llamar a cualquiera de los atributos del modelo mediante la regla del "." y jugar con ellos.
        # aqui estoy guardando los cambios que hice dentro de la base de datos
        # retorno de los datos.
        return super(Add, self).form_valid(form)

class DeleteEmpleado(DeleteView):
    template_name = "persona/DeleteEmpleado.html"
    model = Empleado
    success_url = reverse_lazy("persona_app:correcto")
