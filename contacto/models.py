from django.db import models
import datetime
# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.DecimalField(max_digits=10, decimal_places=0, null=False)  #obligatorio
    ciudad = models.CharField(max_length=25)
    telefono = models.DecimalField(max_digits=10, decimal_places=0)
    mail = models.CharField(max_length=150)
    profesion = models.CharField(max_length=50)
    dependencia = models.CharField(max_length=40)
    cargo = models.CharField(max_length=50)
    archivo = models.FileField(upload_to="archivos/%Y/%m/%d")

#======================================================
#    def __str__(self):
#        return self.user.profile.rol.descripcion
