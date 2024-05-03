
from django.shortcuts import render, redirect

from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    return render(request, "accounts/login.html")


# Create your views here.
def account(request):
    return render(request, "accounts/cadastro.html")


def logout(request):
 
    return redirect('index')