from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.db.models import Q  # Add this line
from .models import Cargo, Socio, Mensalidade
from validate_docbr import CPF
from .forms import SocioForm



def pageSocio(request):
    context = {'is_page_admin':True}
    return render(request, 'admin/socios/socios.html', context)


def verificaCargoSocio(nome_cargo: str):
    """ So deve existir um cargo com os nomes (Presidente,1º Diretor, 2º Diretor,Suplente, Fiscal , Tesoureiro e Secretario ) """
    cargos = ['Presidente','1º Diretor','2º Diretor','Suplente','Fiscal','Tesoureiro','Secretario']
    for cargo in cargos:
        if nome_cargo == cargo:
            if Cargo.objects.filter(nome_cargo = nome_cargo).exists():
                return True
            else:
                return False

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
            if verificaCargoSocio(cargo):
                messages.warning(request, "Ja existe um sócio com  esse cargo ")
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
                mensalidade = Mensalidade.objects.create(nome_socio = socios)
                mensalidade.save()
                messages.success(request, "Socio cadastrado com sucesso!")
                return render(request, 'admin/socios/socios.html')
    return render(request, 'admin/socios/socios.html')
    

def searchSocio(request):
    socio = Socio.objects.all()
    busca = request.GET.get('termo')
    situacao = request.GET.get('situacao')  # Get the value of the 'situacao' parameter

    if busca:
        socio = Socio.objects.filter(Q(nomeCompleto__icontains=busca) | Q(cpf__icontains=busca))

        if situacao:
            if situacao == 'ativo':
                socio = socio.filter(situacao=True)
            elif situacao == 'inativo':
                socio = socio.filter(situacao=False)

        if socio:
            messages.success(request, "Socio encontrado!")
            return render(request, 'admin/socios/buscar_socios.html', {'socios': socio})
        else:
            messages.error(request, "Nenhum socio encontrado!")
            return render(request, 'admin/socios/buscar_socios.html', {'socios': socio})

    return render(request, 'admin/socios/buscar_socios.html', {'socios': socio})

""" 
def searchSocio(request):
    socio = Socio.objects.filter(situacao=True)    
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

 """
def view_socio(request, id):
    socio = get_object_or_404(Socio, id = id)
    print("socio->",socio)
    return render(request, 'admin/socios/buscar_socios.html', {'socio':socio})


def edit_socio(request, id):
    socio = get_object_or_404(Socio, id = id)
    form = SocioForm( instance=socio)
    
    context = {'form_socio':form,'socio':socio}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Socio atualizado com sucesso!")
            return render(request, 'admin/socios/edita_socio.html', context )
        else:
            messages.warning(request, "Erro ao atualizar o sócio!")
            return render(request, 'admin/socios/edita_socio.html', context)
    
    return render(request, 'admin/socios/edita_socio.html', context)



def delete_socio(request, id):
    """ Deve apenas desativar o sócio e fazer com que ele não apareça mais na lista de sócios """

    socio = get_object_or_404(Socio, id=id)
    socio.delete()
    messages.success(request, 'Sócio removido com sucesso!')
    return redirect('socios:BuscarSocio')

    
    
    
    


def monthly_payment(request):
    monthly_payment = Mensalidade.objects.all()

    return render(request,  "admin/socios/mensalidade.html", {"payment":monthly_payment})