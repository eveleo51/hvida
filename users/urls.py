from django.urls import path
from.views import signup, ActivateUser, templateEmailSent, UserList
from contacto.views import UserAppCreate, UserAppView
#, UserApp
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUser, name='activate'),
    path('emailsent/<str:username>/', templateEmailSent, name='emailsent'),
    path('listar/', UserList.as_view(), name="listar"),
    path('listcontact/', UserAppView.as_view(), name="listcontact"),
    path('userapp/', UserAppCreate.as_view(), name="userapp")
]
