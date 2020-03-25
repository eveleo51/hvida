from django.urls import path
from.views import signup, ActivateUser, templateEmailSent, UserList
from django.contrib.auth.decorators import login_required
from . import views
# from contacto.views import UserAppView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUser, name='activate'),
    path('emailsent/<str:username>/', templateEmailSent, name='emailsent'),
    path('listar/', login_required(views.UserList.as_view()), name='listar'),  #Protegemos la url de listado de usuarios
]
