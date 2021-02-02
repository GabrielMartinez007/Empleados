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

class inicioView(TemplateView):
    """"Vista que carga ventana de inicio"""
    template_name = "inicio.html"

class SuccessErasedView(TemplateView):
    template_name = "successErased.html"

class ListAll(ListView):
    template_name = "persona/ListAll.html"
    paginate_by = 6
    ordering = "first_Name"
    context_object_name = "Page"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("key", " ")
        lista = Empleado.objects.filter(
            full_Name__icontains=palabra_clave
        )

        return lista

class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = "persona/detailEmpleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetail, self).get_context_data(**kwargs)
        context['titulo'] = "Empleado del mes"
        return context

class ListByArea(ListView):
    template_name = "persona/ListBy.html"
    context_object_name = "departamento"

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            department__short_name=area
        )

        return lista

class Administrar(ListView):
    template_name = "persona/admin.html"
    model = Empleado
    paginate_by = 6

    def get_queryset(self):
        palabra_clave = self.request.GET.get("key","")
        lista = Empleado.objects.filter(
        full_Name__icontains = palabra_clave
        )

        return lista

class DeleteEmpleado(DeleteView):
    template_name="persona/DeleteEmpleado.html"
    model = Empleado
    success_url = reverse_lazy("persona_app:erased")

class UpdateEmpleado(UpdateView):
    template_name = "persona/UpdateEmpleado.html"
    model = Empleado
    fields = [
        "first_Name",
        "last_Name",
        "job",
        "department",
        "Habilidades",
        "avatar",
    ]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #logica.....
        print("metodo post **************************")
        print(request.POST)
        print(request.POST["first_Name"])
        #logica......
        return super().post(request, *args, **kwargs)

        def form_valid(self, form):


            return super(Add, self).form_valid(form)
    success_url = reverse_lazy("persona_app:erased")

class CreateEmpleado(CreateView):
    template_name = "persona/CreateEmpleado.html"
    model = Empleado
    fields = [
        "first_Name",
        "last_Name",
        "job",
        "department",
        "Habilidades",
        "avatar",
    ]
    success_url = reverse_lazy("persona_app:erased")

    def form_valid(self, form):
        nEmpleado = form.save(commit=False)
        nEmpleado.full_Name = nEmpleado.first_Name + " " + nEmpleado.last_Name
        nEmpleado.save()

        return super(CreateEmpleado, self).form_valid(form)
