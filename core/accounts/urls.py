from django.urls import path
from . import views

app_name = "accounts"
# rota da pagina de lista de contados
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.account, name='cadastro'),
]