from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto, Categorias, Socio
from .forms import ProjetoForm

def add_projeto(request):
    if request.method == 'POST':
        titulo = request.POST.get('tituloProjeto')
        instituicao = request.POST.get('instituicao')
        arquivo_projeto = request.FILES.get('pdf')
        cnpj = request.POST.get('rg')
        data_inicio = request.POST.get('dataInicio')
        data_fim = request.POST.get('dataFim')
        categoria_nome = request.POST.get('categoria')
        participante_id = request.POST.get('participante')

        if not titulo or not instituicao or not arquivo_projeto or not cnpj or not data_inicio or not data_fim or not categoria_nome or not participante_id:
            messages.warning(request, "Todos os campos devem ser preenchidos.")
            return render(request, 'admin/projeto/addProjeto.html')

        try:
            participante = Socio.objects.get(id=int(participante_id))
        except Socio.DoesNotExist:
            messages.warning(request, "Participante não encontrado.")
            return render(request, 'admin/projeto/addProjeto.html')

        projeto = Projeto.objects.create(
            titulo=titulo,
            nome_instituicao=instituicao,
            arquivo_projeto=arquivo_projeto,
            data_inicio=data_inicio,
            data_final=data_fim,
            categoria=categoria_nome,
            participante=participante,
            situacao=True
        )
        projeto.save()

        messages.success(request, "Projeto cadastrado com sucesso!")
        return redirect('projeto:AdcionarProjeto')
    
    participantes = Socio.objects.all()
    context = {'participantes': participantes}
    return render(request, 'admin/projeto/addProjeto.html', context)

def update_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, "Projeto atualizado com sucesso!")
            return redirect('projeto:buscar-projeto')
        else:
            messages.warning(request, "Erro ao atualizar o projeto. Verifique os dados e tente novamente.")
    else:
        form = ProjetoForm(instance=projeto)

    context = {
        'form': form,
        'projeto': projeto
    }
    return render(request, 'admin/projeto/edit_projeto.html', context)

def search_projeto(request):
    projetos = Projeto.objects.all()
    termo = request.GET.get('termo')
    if termo:
        projetos = Projeto.objects.filter(titulo__icontains=termo)
        if projetos.exists():
            messages.success(request, "Projetos encontrados!")
        else:
            messages.error(request, "Nenhum projeto encontrado!")
    else:
        messages.info(request, "Digite um termo de busca para encontrar projetos.")
    return render(request, 'admin/projeto/buscar_projeto.html', {'projetos': projetos})

def delete_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, "Projeto removido com sucesso!")
        return redirect('projeto:buscar-projeto')
    else:
        messages.error(request, "Método não permitido para esta ação.")
        return redirect('projeto:buscar-projeto')
