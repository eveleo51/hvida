from django.urls import path
from.views import signup, ActivateUser, templateEmailSent, UserList
from contacto.views import UserAppCreate, UserAppView
from django.contrib.auth.decorators import login_required
from . import views

#, UserApp
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUser, name='activate'),
    path('emailsent/<str:username>/', templateEmailSent, name='emailsent'),
    path('listar/', login_required(views.UserList.as_view()), name='listar'),  #Protegemos la url de listado de usuarios
    path('listcontact/', login_required(UserAppView.as_view()), name='listcontact'),  #Protegemos las url de listado de contactos
    path('userapp/', login_required(UserAppCreate.as_view()), name='userapp'),  #Protegemos las url de agregar hoja de vida
]
