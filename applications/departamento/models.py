from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField("Nombre", max_length=50)
    short_name = models.CharField("Nombre corto", max_length=20)
    state = models.BooleanField("Estado", default=False)

    class Meta:
        verbose_name = "Mis departamentos"
        verbose_name_plural = "Areas de la empresa"
        ordering = ['name']
        unique_together = ("name", "short_name")


    def __str__(self):
        return self.name 
