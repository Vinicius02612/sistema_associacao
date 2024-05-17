from django.urls import path
from . import views

app_name = "socios"
# rota da pagina de lista de contados
urlpatterns = [
    path('', views.pageSocio, name='socios'),
    path('search_socio/', views.searchSocio, name='BuscarSocio'),
    #path('/vew_socio', views.searchSocio, name='VerSocio'),
]