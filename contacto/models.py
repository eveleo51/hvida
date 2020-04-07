from django.db import models
import datetime
# Create your models here.
#Tabla para el almacenamiento de cargos
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#Tabla para el almacenamiento de dependencias
class Dependencia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#Tabla para el almacenamiento de contactos
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.DecimalField(max_digits=10, decimal_places=0, null=False)  #obligatorio
    ciudad = models.CharField(max_length=25)
    telefono = models.DecimalField(max_digits=10, decimal_places=0)
    mail = models.CharField(max_length=150)
    profesion = models.CharField(max_length=50)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    archivo = models.FileField(upload_to="archivos/%Y/%m/%d", null=False)

    def __str__(self):
        return self.nombre

    def get_success_url(self):
        return reverse('')
