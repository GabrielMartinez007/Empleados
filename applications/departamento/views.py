from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .form import NewDepartment
from applications.persona.models import Empleado
from .models import Department
# Create your views here.

class Listar_Dep(ListView):
    template_name = "departamento/departamentos.html"
    model = Department
    context_object_name = "dep"
