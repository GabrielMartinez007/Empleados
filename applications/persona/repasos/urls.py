from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path('listAll/', views.ListAll.as_view()),
    path('listByKey/', views.ListbyKey.as_view()),
    path('buscarHabs/', views.BuscarHabsEmpleado.as_view()),
    path('verEmpleado/<pk>', views.EmpleadoDetail.as_view()),
    path('Adds/', views.Add.as_view()),
    
    path(
        'success/',
        views.Success.as_view(),
        name="correcto"
    ),
    path(
        'update/<pk>',
        views.UpdateEmpleado.as_view(),
        name="actualizar"
    ),
    path(
        'delete/<pk>',
        views.DeleteEmpleado.as_view(),
        name="borrar"
    ),

]
