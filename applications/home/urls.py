from django.urls import path

from . import views

# aqui se iran agregando las urls que usaran las aplicaciones (hay que hacer referencia este archivo urls desde el
# urls principal

urlpatterns = [

    # la sintaxis para hacer referencia a una vista es, (referencia al archivo de las vistas "views", luego . la
    # clase que tiene la vista luego . as_view)

    path('prueba/', views.Test.as_view()),
    path('lista/', views.Lista.as_view()),
    path('listar-prueba/', views.ListPrueba.as_view()),
    path('add/', views.CreatePrueba.as_view()),
    path(
        'resumeFound/',
        views.resumeFound.as_view(),
        name="resumeFound"
        )
]
