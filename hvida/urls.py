from django.contrib import admin
from django.urls import path, include
from contacto import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name=""),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:pk>/', views.BadgetUpdate.as_view(), name='editar'),
    path('crear/', views.BadgetCreate.as_view(), name='crear'),
    path('eliminar/<int:pk>/', views.BadgetDelete.as_view(), name='eliminar'),
    path('users/', include(('users.urls','users'), namespace='users')),
    path('userapp/', UserAppCreate.as_view(), name="userapp")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
