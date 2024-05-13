from django.shortcuts import render

def homePage(request):
    return render(request, 'homePage/index.html', {})

def addSocio(request):
    return render(request, 'addSocio/index.html')

def searchSocio(request):
    socios = [
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Socio"},
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

def searchProjeto(request):
    projetos = [
        {"titulo": "Cultura Afro", "cnpj": "405.896.008-73", "nome_intituicao": "TecnoAgro", "data_inicio": "30/09/2022", "data_conclusao": "30/12/2023", "status": "Concluído"},
        {"titulo": "Cultura Afro", "cnpj": "405.896.008-73", "nome_intituicao": "TecnoAgro", "data_inicio": "30/09/2022", "data_conclusao": "30/12/2023", "status": "Concluído"},
        {"titulo": "Cultura Afro", "cnpj": "405.896.008-73", "nome_intituicao": "TecnoAgro", "data_inicio": "30/09/2022", "data_conclusao": "30/12/2023", "status": "Concluído"},
        {"titulo": "Cultura Afro", "cnpj": "405.896.008-73", "nome_intituicao": "TecnoAgro", "data_inicio": "30/09/2022", "data_conclusao": "30/12/2023", "status": "Concluído"},
        {"titulo": "Cultura Afro", "cnpj": "405.896.008-73", "nome_intituicao": "TecnoAgro", "data_inicio": "30/09/2022", "data_conclusao": "30/12/2023", "status": "Concluído"},
            
    ]
    return render(request, 'searchProjeto/index.html', {'projetos': projetos})

def mensalidades(request):
    mensalidades = [
        {"nome": "José Pedro", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Presidente"},
        {"nome": "João Carlos", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Atrasada", "cargo": "Sócio"},
        {"nome": "Miguel", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Em dia", "cargo": "Vice Presidente"},
        {"nome": "Vinicius Nunes", "cpf": "405.896.008-73", "rg": "12.078.765-9", "data_nascimento": "30/09/2002", "mensalidade": "Atrasada", "cargo": "Sócio"},
       
    ]
    return render(request, 'mensalidades/index.html', {'mensalidades': mensalidades})