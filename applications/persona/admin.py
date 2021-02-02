from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = [
        'first_Name',
        'last_Name',
        'department',
        'job',
        'id',
    ]
admin.site.register(Empleado, EmpleadoAdmin)
