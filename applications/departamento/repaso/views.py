from django.shortcuts import render
from django.views.generic.edit import FormView
from .form import NewDepartment
from applications.persona.models import Empleado
from .models import Department
# Create your views here.

class newRegisterDepartment(FormView):
    template_name = "departamento/newRegister.html"
    form_class = NewDepartment
    success_url = "/"

    # Form_valid sirve para trabajar con los datos traidos en el formulario antes de que llegue a los modelos
    # En este caso estoy trabajando con dos modelos a la vez ya que los datos pertenecen a dos modelos diferentes
    def form_valid(self, form):
        # esta es una forma de crear un registro en un modelo, basicamente es crear una instancia del modelo
        # la misma recibe como parametros los campos que tiene el modelo
        departamento = Department(
            # dentro de form.cleaned_data[] estaran los datos traidos por el formulario
            # por parametro debe pasearsele a la tupla el nombre que se le asigno al formulario
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shortName']
        )
        # para que los realizados dentro de la instancia se guarden es necesario llamar al metodo save
        departamento.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        # esta es otra forma de crear un registro dentro de la base de datos, solo es llamar (modelo.objects.create)
        # asi no es necesario usar save ni nada, de ahi solo es llamar los campos del modelo y llenarlos.
        Empleado.objects.create(
            first_Name = nombre,
            last_Name = apellido,
            job = '1',
            department = departamento

        )
        return super(newRegisterDepartment, self).form_valid(form)
