from django.urls import path
from . import views

app_name = "socios"
# rota da pagina de lista de contados
urlpatterns = [
    path('', views.homePage, name='HomeSocio'),
    path('add_socio/', views.addSocio, name='AdiconarSocio'),
    path('search_socio/', views.searchSocio, name='BuscarSocio'),
    #path('/vew_socio', views.searchSocio, name='VerSocio'),
]