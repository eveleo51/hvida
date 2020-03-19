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
    path('', login_required(views.UserList.as_view()), name='index'),  #Protegemos las urls de Userapp Probando 123....
#    path('', login_required(views.base.as_view()), name='index'),  #Protegemos las urls de Userapp Probando 123....
#    path('', login_required('auth:users'), name='index'),  #Protegemos las urls de Userapp Probando 123....
    path('listar/', UserList.as_view(), name="listar"),
    path('listcontact/', UserAppView.as_view(), name="listcontact"),
    path('userapp/', UserAppCreate.as_view(), name="userapp")
]
