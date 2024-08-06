from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Projeto
from datetime import datetime
from .forms import FormProjeto



# Create your views here.
def home_page(request):
    form = FormProjeto()

    if request.method == 'POST':
        form = FormProjeto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Projeto cadastrado com sucesso!")
            return redirect('projeto:AdcionarProjeto')
        else:
            messages.error(request, "Erro ao cadastrar projeto!")
            return render(request, 'admin/projeto/addProjeto.html', {'form': form})
    return render(request, 'admin/projeto/addProjeto.html', {'form': form})
        
        


def upadate_projeto(request, id):
    projeto = Projeto.objects.get(id=id)
    form = FormProjeto(request.POST, request.FILES, instance=projeto)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Projeto atualizado com sucesso!")
            return redirect('projeto:buscar-projeto')
        else:
            messages.error(request, "Erro ao atualizar projeto !")
            return render(request, 'admin/projeto/atualizar_projeto.html',{ 'projeto': projeto,'form':form})
    else:
        form = FormProjeto(instance=projeto)
        return render(request, 'admin/projeto/atualizar_projeto.html',{ 'projeto': projeto, 'form':form})


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
    