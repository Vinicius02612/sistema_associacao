from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .models import Cargo, Socio, Mensalidade
from validate_docbr import CPF
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
        
        _cpf = CPF()
        if  _cpf.validate(cpf) is not True:
            messages.warning(request, "CPF inválido ")
            return render(request, 'admin/socios/socios.html')
    

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
            mensalidade = Mensalidade.objects.create(nomeCompleto=nome)
            mensalidade.save()
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

def update_socios(request, id):

    socio = get_object_or_404(Socio, id = id)
    form_socio = SocioForm(request.POST)
    if request.method == 'POST':

        if(form_socio.is_valid()):
            form_socio.save()
            messages.success(request, "Socio atualizado com suecesso!")
            return render(request, 'admin/socios/buscar_socios.html',{'form':form_socio, 'socios':socio })
    return render(request, 'admin/socios/edita_socio.html', {'form':form_socio, 'socios':socio })


def monthly_payment(request):
    monthly_payment = Mensalidade.objects.all()

    search_payment_name = request.GET.get('termo')
    if monthly_payment:
        monthly_payment = Mensalidade.objects.filter(monthly_payment_icontains= search_payment_name)
        if monthly_payment:
            messages.success(request,"Mensaliade encontrada")
            return render(request,  "admin/socios/mensalidade.html", {"payment":monthly_payment})
    return render(request, "admin/socios/mensalidade.html")