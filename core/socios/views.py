from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Cargo, Socio
from django.db.models.functions import Concat
from django.db.models import Q, Value
from .forms import SocioForm


def pageSocio(request):
    return render(request, 'admin/socios/socios.html')

def addPartners(request):
    if request.method == 'POST':
        
        nome = request.POST.get('nomeCompleto')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
        rg = request.POST.get('rg')
        declaracao = request.POST.get('declaracao')
        data_nascimento = request.POST.get('dataNascimento')
        cargo = request.POST.get('cargo')
        atividade = request.POST.get('atividade')
        qtdPessoas = request.POST.get('quantidadePfamilia')
        status = True
        
        if not nome or not cpf or not sexo or not rg or not declaracao or not data_nascimento or not cargo or not atividade or not qtdPessoas:
            messages.warning(request, "Todos os campos devem ser preenchidos ")
            return render(request, 'admin/socios/socios.html')
        
        if Socio.objects.filter(cpf = cpf).exists():
            messages.warning(request, "Ja existe um sócio com  esses dados ")
            return render(request, 'admin/socios/socios.html')
        else:
            cargos = Cargo.objects.create(nome_cargo = cargo)
            cargos.save()
            socios = Socio.objects.create(
                nomeCompleto=nome,
                cpf=cpf,
                dataNascimento=data_nascimento,
                sexo=sexo,
                registro=rg,
                arq_autoDeclaracao=declaracao,
                atividade_agr=atividade,
                quantidade_pessoa=qtdPessoas,
                cargo=cargos,
                situacao=status
            )
            
            socios.save()
            messages.success(request, "Socio cadastrado com sucesso!")
            return render(request, 'admin/socios/socios.html')
    return render(request, 'admin/socios/socios.html')
    

def searchSocio(request):
    socio = Socio.objects.all()
    
    busca = request.GET.get('termo')
    if busca:
        socio = Socio.objects.filter(nomeCompleto__icontains = busca)
        if socio:
            messages.success(request, "Socio encontrado!")
            return render(request, 'admin/socios/buscar_socios.html',{'socios':socio})
        else:
            messages.error(request, "Nenhum socio encontrado!")
            return render(request, 'admin/socios/buscar_socios.html',{'socios':socio})

    return render(request, 'admin/socios/buscar_socios.html',{'socios':socio})
    

def remover_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.delete()
    messages.success(request, 'Sócio removido com sucesso!')
    return redirect('socios:BuscarSocio')


from django.template import TemplateDoesNotExist

def edit_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    if request.method == 'POST':
        form = SocioForm(request.POST, request.FILES, instance=socio)  # Incluindo request.FILES para lidar com arquivos
        if form.is_valid():
            form.save()
            messages.success(request, 'Sócio atualizado com sucesso!')
            return redirect('socios:BuscarSocio')
    else:
        form = SocioForm(instance=socio)
    
    try:
        return render(request, 'admin/socios/edit_socio.html', {'form': form, 'socio': socio})
    except TemplateDoesNotExist as e:
        print(f"Template not found: {e}")
        raise e


#def save_edit_socio(request, id):
#    socio = get_object_or_404(Socio, id=id)
#    if request.method == 'POST':
#        socio.nomeCompleto = request.POST.get('nomeCompleto')
#        socio.cpf = request.POST.get('cpf')
#        socio.dataNascimento = request.POST.get('dataNascimento')
#        socio.sexo = request.POST.get('sexo')
#        socio.registro = request.POST.get('registro')
#        socio.cargo = request.POST.get('cargo')
#        socio.arq_autoDeclaracao = request.POST.get('arq_autoDeclaracao')
#        socio.save()
#        return redirect('socios:some_view')  # Redirecionar para a visão desejada após salvar