from django.db import models


class Vehiculo(models.Model):
    marca = models.CharField(verbose_name="marca",max_length=50)
    modelo = models.CharField(verbose_name="modelo",max_length=50)
    año = models.DateField(verbose_name="año")

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.año}"
    
