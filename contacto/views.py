from django.shortcuts import render
from django.urls import reverse
from .models import Contacto
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import DataForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

#funcion para busqueda de empleado por parametro nombre
def searchContacto(request):
    if request.method == 'POST':
        pattern = request.POST['search']
        contacto= Contacto.objects.filter(nombre__contains=pattern)  # buscamos dentro de nombre la palabra que ingresa (contenida)
    return render(request,'auth/contact_list.html',{'object_list':contacto, 'search':pattern})

#Se lista el detalle de una hoja de vida
class UserDetail(PermissionRequiredMixin,DetailView):   # Listar la tabla Contacto
    permission_required = 'users.listarusuarios'       # Protegemos el Ingreso por URL desde el mismo Modulo
    model=Contacto
    template_name = "auth/contact_ver.html"  #"auth/contact_ver.html"

class UserAppUpdate(PermissionRequiredMixin,UpdateView):  # Actualizar la tabla Contacto
    permission_required = 'users.listarusuarios'          # Protegemos el Ingreso por URL desde el mismo Modulo
    model= Contacto
    fields = ['nombre', 'cedula', 'ciudad', 'telefono', 'mail', 'profesion', 'dependencia', 'cargo', 'archivo']
    template_name = "auth/user_app.html"

    def get_success_url(self):  #redirecciona una vez ejecutado el proceso anterior
        return reverse('')

class UserAppCreate(CreateView):  # Agregar a la tabla Contacto
    model= Contacto
    fields = ['nombre', 'cedula', 'ciudad', 'telefono', 'mail', 'profesion', 'dependencia', 'cargo', 'archivo']
    template_name = "auth/user_app.html"

    def get_success_url(self):
        return reverse('')

class UserAppView(PermissionRequiredMixin,ListView):   # Listar la tabla Contacto
    permission_required = 'users.listarusuarios'       # Protegemos el Ingreso por URL desde el mismo Modulo
    model=Contacto
    template_name = "auth/contact_list.html"
    paginate_by = 5        #Defino el numero de elementos por página

    def get_queryset(self):
        # query = Contacto.objects.filter(cedula=1010)
        query = Contacto.objects.all()
        return query

def home(request):
    return render (request,"home.html")  #pagina principal

def about_us(request):
    return render (request,"about_us.html")  #pagina principal
