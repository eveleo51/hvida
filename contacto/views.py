from django.shortcuts import render
from django.urls import reverse
from .models import Contacto
from django.http import HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import DataForm

<<<<<<< HEAD
class UserAppCreate(CreateView):
    model= Contacto
    fields = ['nombre', 'cedula', 'ciudad', 'telefono', 'mail', 'profesion', 'dependencia', 'cargo', 'archivo']
    template_name = "auth/user_app.html"

    def get_success_url(self):  #redirecciona una vez ejecutado el proceso anterior
        return reverse('')

#Este es la clase para Crear los productos
#    def get_success_url(self):
#        return render(request, "auth/user_app.html", {'form': form})
#    def get_success_url(self):  #redirecciona una vez ejecutado el proceso anterior
#        return reverse('')

class UserAppView(ListView):
    model=Contacto
#    context_object_name='listcontact'
    template_name = "auth/contact_list.html"

    def get_queryset(self):
        # query = Contacto.objects.filter(cedula=1010)
        query = Contacto.objects.all()
        return query

=======

#class ListarProductos(ListView):
#    template_name = 'user_app.html'

class Badgetview(ListView):
    model='user_app.html'  #pagina de registrados
    context_object_name='listcontac'

    def get_queryset(self):
        query = contacto.objects.filter(cedula=10203040)
        return query

#Este es la clase para Crear los productos
class BadgetCreate(CreateView):
    model= Contacto
    form = DataForm()
#    return render(request, 'auth/user_app.html', {'form': form})
#    model = 'user_app.html'  #pagina de registrados
#    fields = ['nombre','cedula','ciudad','telefono','mail','profesion','dependencia','cargo','archivo']
#    def UserApp(request):
    def get_success_url(self):
        return render(request, "auth/user_app.html", {'form': form})


>>>>>>> 2abdc2136b00fa8c3d7b3e9173a0c1d97a1bea15
#    def get_success_url(self):  #redirecciona una vez ejecutado el proceso anterior
#        return reverse('')

class BadgetUpdate(UpdateView):
    model = 'user_app.html'  #pagina de registrados
    fields = ['nombre','cedula','ciudad','telefono','mail','profesion','dependencia','cargo','archivo']

    def get_success_url(self):
        return reverse('')

class BadgetDelete(DeleteView):
    model = 'user_app.html'  #pagina de registrados

    def get_success_url(self):
        return reverse('')

def home(request):
    return render (request,"home.html")


class UserAppCreate(CreateView):
    model= Contacto
    fields = ['nombre', 'cedula', 'ciudad', 'telefono', 'mail', 'profesion', 'dependencia', 'cargo', 'archivo']
    template_name = "auth/user_app.html"
