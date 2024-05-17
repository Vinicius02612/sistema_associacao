from django.urls import path
from . import views

app_name = "pageadmin"

urlpatterns = [
    path('', views.page, name='page'),
]