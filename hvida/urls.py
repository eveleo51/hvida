from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from contacto import views
from contacto.views import UserAppCreate, UserAppUpdate, UserAppView, UserAppMostrar

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name=""),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('crear/', login_required(views.UserAppCreate.as_view()), name='crear'),  #Protegemos las url desde modo incognito
    path('<int:pk>/', login_required(UserAppUpdate.as_view()), name='editar'),  # llamamos el metodo UserAppUpdate con el alias editar
    path('<int:pk>/', login_required(UserAppMostrar.as_view()), name='vercontacto'),  # llamamos el metodo UserAppMostrar con el alias ver
    path('listcontact/', login_required(UserAppView.as_view()), name='listcontact'),
    path('users/', include(('users.urls','users'), namespace='users')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
