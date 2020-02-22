from django.urls import path
<<<<<<< HEAD
from.views import signup, ActivateUser, templateEmailSent, UserList
from contacto.views import UserAppCreate, UserAppView
#, UserApp
=======
from.views import signup, ActivateUser, templateEmailSent, UserList, UserApp

>>>>>>> 2abdc2136b00fa8c3d7b3e9173a0c1d97a1bea15
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUser, name='activate'),
    path('emailsent/<str:username>/', templateEmailSent, name='emailsent'),
    path('listar/', UserList.as_view(), name="listar"),
    path('listcontact/', UserAppView.as_view(), name="listcontact"),
    path('userapp/', UserAppCreate.as_view(), name="userapp")
]
