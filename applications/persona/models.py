from django.db import models
from applications.departamento.models import Department


# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField("Habilidades", max_length=50)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades de empleados"

    def __str__(self):
        return  self.habilidad


class Empleado(models.Model):

    Job_Choices = [
        ("0", "Contador"),
        ("1", "Administrador"),
        ("2", "Economista"),
        ("3", "Otro"),
        ("4", "Ladron")
    ]

    first_Name = models.CharField("Nombre", max_length=50)
    last_Name = models.CharField("Apellido", max_length=50)
    full_Name = models.CharField("Nombre completo", max_length=120, blank=True)
    job = models.CharField("Cargo", max_length=1, choices=Job_Choices)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    Habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = "Mis empleados"
        verbose_name_plural = "Empleados de la empresa"
        ordering = ['-first_Name', 'last_Name']
        unique_together = ("first_Name", "department")

    def __str__(self):
        return str(self.id) + "-" + self.first_Name + "-" + self.last_Name + "-" + str(self.department.short_name)
