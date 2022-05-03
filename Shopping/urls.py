from django.urls import path
from Shopping import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('locales/', views.locales, name="Locales"),
    path('patioDeComidas/', views.patioComidas, name="PatioDeComidas"),
    path('cine/', views.cine, name="Cine"),
    path('promociones/', views.promociones, name="Promociones"),
    path('registro/', views.registro, name="Registro"),
    path('formulario/', views.formulario, name="Formulario"),
    path('busquedaUsuario/', views.busquedaUsuario, name="BusquedaUsuario"),
    #path('buscar/', views.buscar),

   
]
