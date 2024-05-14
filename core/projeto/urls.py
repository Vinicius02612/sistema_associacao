from django.urls import path
from . import views

app_name = "projeto"
# rota da pagina de lista de contados
urlpatterns = [
    path('', views.homePage, name='porjeto'),
    path('add_projeto/', views.addProjeto, name='AdcionarProjeto'),
    #path('search_projeto/', views.searchSocio, name='BuscarPorjeto'),
]