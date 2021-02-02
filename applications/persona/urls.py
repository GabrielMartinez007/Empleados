from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('',
        views.inicioView.as_view(),
        name="Inicio"
    ),

    path('listar-todo/',
        views.ListAll.as_view(),
        name="Lista"
    ),

    path('verEmpleado/<pk>',
        views.EmpleadoDetail.as_view(),
        name="detalleEmpleado"),

    path(
        'EmpleadoArea/<short_name>/',
        views.ListByArea.as_view(),
        name="listarArea"
    ),

    path(
        'administrador/',
        views.Administrar.as_view(),
        name="administrar"
    ),

    path(
        'borrado/<pk>',
        views.DeleteEmpleado.as_view(),
        name="eliminado"
    ),

    path(
        'elimiadoCorrecto/',
        views.SuccessErasedView.as_view(),
        name="erased"
    ),

    path(
        'updateEmpleado/<pk>',
        views.UpdateEmpleado.as_view(),
        name="update"
    ),

    path(
        'CreateEmpleados/',
        views.CreateEmpleado.as_view(),
        name="crear"
    ),
]
