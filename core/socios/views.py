from django.shortcuts import render
from django.contrib import messages
from .models import Cargo, Socio
from django.db.models.functions import Concat
from django.db.models import Q, Value
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

