from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path('', views.piloto_lista, name='piloto_lista'),
    path('pilotos/nuevo/', views.piloto_crear, name='piloto_crear'),
    path('pilotos/<int:pk>/', views.piloto_detalle, name='piloto_detalle'),
    path(
        'pilotos/<int:pk>/editar/',
        views.piloto_editar,
        name='piloto_editar',
    ),
    path(
        'pilotos/<int:pk>/eliminar/',
        views.piloto_eliminar,
        name='piloto_eliminar',
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='modulo/login.html'
        ),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
