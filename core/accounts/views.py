
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):

    path = "accounts/login.html"
    pathAdmin = "admin/home/home.html"
    if request.method != "POST":
        return render(request, path)
    else:
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=user,password=password)
        if not user:
            messages.error(request, 'Usuário ou senha inválida, tente novamente!')
            return render(request, path)
        else:
            auth.login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return render(request, pathAdmin)
    



# Create your views here.
def account(request):
    return render(request, "accounts/cadastro.html")


def logout(request):
    path = "accounts/login.html"
    return render(request,path)