"""
URL configuration for TercerEntregaPiyuka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Este punto nos permite configurar los puntos de entrada para que los usuarios intetactuen con nuestra plataforma
Enviando solicitudes
"""
from django.contrib import admin
from django.urls import path,include
from .views import inicio, usuarios, crear_usuario, cargar_torrent, buscar_torrents, descargar_torrent, eliminar_torrent, detalles_torrent
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='home'),
    path('usuarios/', usuarios, name='usuarios'),
    path('crear-usuario/', crear_usuario, name='crear_usuario'),
    path('cargar-torrent/', cargar_torrent, name='cargar_torrent'),
    path('buscar-torrents/', buscar_torrents, name='buscar_torrents'),
    path('descargar-torrent/<int:torrent_id>/', descargar_torrent, name='descargar_torrent'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('eliminar-torrent/<int:torrent_id>/', eliminar_torrent, name='eliminar_torrent'),
    path('detalles-torrent/<int:torrent_id>/', detalles_torrent, name='detalles'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)