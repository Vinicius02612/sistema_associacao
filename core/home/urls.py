from django.urls import path
from . import views

app_name = "home"
# rota da pagina de lista de contados
urlpatterns = [
    path('', views.home, name='home'),
]