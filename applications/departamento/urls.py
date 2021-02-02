from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path(
        'departamento/',
        views.Listar_Dep.as_view(),
        name="departamentos"),
]
