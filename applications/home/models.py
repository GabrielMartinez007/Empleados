from django.db import models


# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

# Esta funcion sirve para definir el campo que hara referencia a todos el registro
    def __str__(self):
        return self.titulo + "-" + self.subtitulo

# Para hacer migracion de la base de datos(que se aplique en la base de datos) primero desde el entorno virtual y en
# la carpeta del projecto debo ejecutar el comando "python manage.py makemigrations" asi se comprobaran los cambios,
# luego ejecutamos el comando "python manage.py migrate"
# de esa manera se crean tablas dentro de la base de datos en django
