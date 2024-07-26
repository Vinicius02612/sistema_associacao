from django.urls import path
from . import views

app_name = "socios"
# rota da pagina de lista de contados
urlpatterns = [
    path('', views.pageSocio, name='socios'),
    path('add_socio/', views.addPartners, name='add_socio'),
    path('search_socio/', views.searchSocio, name='BuscarSocio'),
    #path('edit_socio/<int:id>/edit', views.update_socios, name='editSocio'),
    path('edit/<int:id>/', views.edit_socio, name='editSocio'),
 
    path('remover/<int:id>/', views.remover_socio, name='removerSocio'),
]