from django.shortcuts import render

from django.contrib import messages
from .models import Projeto, Categorias
from django.db.models.functions import Concat
from django.db.models import Q, Value
from datetime import datetime
import time

def check_date(date_begin, date_end):
    print(date_begin, date_begin)

    dt_begin = datetime.strptime(date_begin,'%Y-%m-%d').date()
    dt_end = datetime.strptime(date_end,'%Y-%m-%d').date()

    
    is_bigger = False

    if dt_end <= dt_begin:
        is_bigger = True

    return is_bigger


# Create your views here.
def home_page(request):
    if request.method == 'POST':
        title_project = request.POST.get("title_project")
        name_instituty = request.POST.get("name_instituty")
        document_project = request.POST.get("document_project")
        cnpj_user = request.POST.get("cnpj_user")
        date_begin = request.POST.get("date_begin")
        date_end = request.POST.get("date_end")
        category = request.POST.get("categoria")
        data = [title_project,name_instituty,document_project,cnpj_user,date_begin,date_end, category]
        if data is None:
            messages.warning(request, "Todos os campos devem ser preenchidos")
            return render(request, 'admin/projeto/addProjeto.html')
        
        if check_date(date_begin=date_begin, date_end=date_end) is True:
            messages.warning(request, "Data de inicio não pode ser menor que a final")
            return render(request, 'admin/projeto/addProjeto.html')
        else:
            status = True
            category = Categorias.objects.create(nome=category)
            category.save()
            project = Projeto.objects.create(
                titulo = title_project,
                nome_instituicao = name_instituty,
                arquivo_projeto = document_project,
                cnpj = cnpj_user,
                data_inicio = date_begin,
                data_final = date_end,
                situacao = status,
                categoria = category,
            )
            project.save()
            messages.success(request, "Projeto cadastrado com sucesso!")
        
    return render(request, 'admin/projeto/addProjeto.html')

def upadate_projeto(request):
    return render(request, 'admin/projeto/atualizar_projeto.html')


def search_projeto(request):
    projeto = Projeto.objects.all()
    
    busca = request.GET.get('termo')
    if busca:
        projeto = Projeto.objects.filter(titulo__icontains = busca)
        if projeto:
            messages.success(request, "Projeto encontrado !")
            return render(request, 'admin/projeto/buscar_projeto.html',{'projetos':projeto})
        else:
            messages.error(request, "Nenhum socio encontrado!")
            return render(request, 'admin/projeto/buscar_projeto.html',{'projetos':projeto})
    return render(request, 'admin/projeto/buscar_projeto.html',{'projetos':projeto})
    