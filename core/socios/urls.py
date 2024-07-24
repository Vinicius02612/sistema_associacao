from django.urls import path
from . import views

app_name = "socios"
# rota da pagina de lista de contados
urlpatterns = [
    path('', views.pageSocio, name='socios'),
    path('add_socio/', views.addPartners, name='add_socio'),
    path('search_socio/', views.searchSocio, name='BuscarSocio'),
    path('edit_socio/<int:id>/edit', views.edit_socio, name='editSocio'),
    path('delete_socio/<int:id>/delete', views.delete_socio, name='deleteSocio'),
    path('mensalidade/', views.monthly_payment, name='mensalidade'),

]