from django.urls import path
from . import views

app_name = "projeto"
# rota da pagina de lista de contados
urlpatterns = [
    path('add_projeto/', views.add_projeto, name='AdcionarProjeto'),
    path('atualizar_projeto/<int:id>/', views.upadate_projeto, name='atualizar-projeto'),
    path('search_projeto/', views.search_projeto, name='buscar-projeto'),
    path('delete_projeto/<int:id>/', views.delete_projeto, name='deletar-projeto'),
]