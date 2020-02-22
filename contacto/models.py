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

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6ef28ef31abdcc475da430903b4593df99bab6f4
    def __str__(self):
        return self.nombre

    def get_success_url(self):
        return reverse('')
<<<<<<< HEAD
=======
=======
#======================================================
def __str__(self):
    return self.nombre

def get_success_url(self):
    return reverse('')
>>>>>>> 2abdc2136b00fa8c3d7b3e9173a0c1d97a1bea15
>>>>>>> 6ef28ef31abdcc475da430903b4593df99bab6f4
