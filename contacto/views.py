from django.shortcuts import render
from django.urls import reverse
from .models import Contacto
from django.http import HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import DataForm


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
