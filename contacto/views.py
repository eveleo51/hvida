from django.shortcuts import render
from django.urls import reverse
from .models import Contacto
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import DataForm

class UserAppCreate(CreateView):
    model= Contacto
    fields = ['nombre', 'cedula', 'ciudad', 'telefono', 'mail', 'profesion', 'dependencia', 'cargo', 'archivo']
    template_name = "auth/user_app.html"
    def get_success_url(self):  #redirecciona una vez ejecutado el proceso anterior

        return reverse('')

class UserAppView(ListView):
    model=Contacto
#    context_object_name='listcontact'
    template_name = "auth/contact_list.html"
    paginate_by = 2

    def get_queryset(self):
        # query = Contacto.objects.filter(cedula=1010)
        query = Contacto.objects.all()
        return query


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
