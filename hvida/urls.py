from django.contrib import admin
from django.urls import path, include
from contacto import views
# from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home, name=""),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:pk>/', views.BadgetUpdate.as_view(), name='editar'),
    path('eliminar/<int:pk>/', views.BadgetDelete.as_view(), name='eliminar'),
    path('users/', include(('users.urls','users'), namespace='users')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#UserAppView
