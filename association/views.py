from django.shortcuts import render

def homePage(request):
    return render(request, 'homePage/index.html', {})

def addSocio(request):
    return render(request, 'addSocio/index.html')

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
    return render(request, 'searchSocio/index.html', {'socios': socios})

def addProjeto(request):
    return render(request, 'addProjeto/index.html')
