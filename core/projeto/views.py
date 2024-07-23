from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto, Categorias, Socio

# Create your views here.
def home_page(request):
    return render(request, 'admin/projeto/addProjeto.html')

def add_projeto(request):
    if request.method == 'POST':
        # Obtendo os dados do formulário
        titulo = request.POST.get('tituloProjeto')
        instituicao = request.POST.get('instituicao')
        arquivo_projeto = request.FILES.get('pdf')
        cnpj = request.POST.get('rg')
        data_inicio = request.POST.get('dataInicio')
        data_fim = request.POST.get('dataFim')
        categoria_id = request.POST.get('categoria')
        participante_id = request.POST.get('participante')

        # Impressão dos dados recebidos
        print(f"Título do Projeto: {titulo}")
        print(f"Nome da Instituição: {instituicao}")
        print(f"Arquivo do Projeto: {arquivo_projeto}")
        print(f"CNPJ: {cnpj}")
        print(f"Data de Início: {data_inicio}")
        print(f"Data de Fim: {data_fim}")
        print(f"Categoria ID: {categoria_id}")
        print(f"Participante ID: {participante_id}")

        # Verificação de campos vazios
        if not titulo or not instituicao or not arquivo_projeto or not cnpj or not data_inicio or not data_fim or not categoria_id or not participante_id:
            messages.warning(request, "Todos os campos devem ser preenchidos.")
            return render(request, 'admin/projeto/addProjeto.html')

        try:
            categoria = Categorias.objects.get(id=categoria_id)
            participante = Socio.objects.get(id=participante_id)
            print("salvou")
        except Categorias.DoesNotExist:
            messages.warning(request, "Categoria não encontrada.")
            print("Erro")
            return render(request, 'admin/projeto/addProjeto.html')
        except Socio.DoesNotExist:
            print(" Não salvou")
            messages.warning(request, "Participante não encontrado.")
            return render(request, 'admin/projeto/addProjeto.html')

        # Criar e salvar o projeto
        projeto = Projeto.objects.create(
            titulo=titulo,
            nome_instituicao=instituicao,
            arquivo_projeto=arquivo_projeto,
            data_inicio=data_inicio,
            data_final=data_fim,
            categoria=categoria,
            participante=participante,
            situacao=True
        )
        projeto.save()


        # Mensagem de sucesso e redirecionamento
        messages.success(request, "Projeto cadastrado com sucesso!")
        return redirect('projeto:AdcionarProjeto')  # Redirecionar para a página de listagem ou outra página
    
    categorias = Categorias.objects.all()
    participantes = Socio.objects.all()  # Certifique-se de que há dados aqui
    context = {
        'categorias': categorias,
        'participantes': participantes
    }
    return render(request, 'admin/projeto/addProjeto.html', context)
    


def upadate_projeto(request):
    return render(request, 'admin/projeto/atualizar_projeto.html')


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
