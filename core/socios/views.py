from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def pageSocio(request):
    return render(request, 'admin/socios/socios.html', {})


def searchSocio(request):
    socios = [
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
        {"nome": "Vinicius Nunes", "cpf": "000.000.000-00", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Sócio"},
    ]
    return render(request, 'socios/buscar_socios.html', {'socios': socios})

