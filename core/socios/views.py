from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Socio, Mensalidade
from validate_docbr import CPF
from .forms import SocioForm
from django.contrib.auth.decorators import login_required


@login_required
def pageSocio(request):
    context = {'is_page_admin':True}
    return render(request, 'admin/socios/socios.html', context)


@login_required
def addPartners(request):
    form_socio = SocioForm()
    if request.method == 'POST':
        
        form_socio = SocioForm(request.POST, request.FILES)
        print(form_socio.arq_autoDeclaracao)
        if form_socio.is_valid():
            form_socio.save()
            messages.success(request, 'Sócio cadastrado com sucesso!')
            return redirect('socios:BuscarSocio')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return render(request, 'admin/socios/socios.html', {'form': form_socio})
    return render(request, 'admin/socios/socios.html', {'form': form_socio})
    
@login_required
def searchSocio(request):
    socio = Socio.objects.all()
    busca = request.GET.get('termo')

    if busca:
        socio = Socio.objects.filter((Q(nomeCompleto__icontains=busca) | Q(cpf__icontains=busca)), situacao=True)

        if socio:
            messages.success(request, "Socio encontrado!")
            return render(request, 'admin/socios/buscar_socios.html', {'socios': socio})
        else:
            messages.error(request, "Nenhum socio encontrado!")
            return render(request, 'admin/socios/buscar_socios.html', {'socios': socio})

    return render(request, 'admin/socios/buscar_socios.html', {'socios': socio})

@login_required
def view_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    if request.method == 'POST':
        form = SocioForm(request.POST, request.FILES, instance=socio)  # Incluindo request.FILES para lidar com arquivos
        if form.is_valid():
            form.save()
            messages.success(request, 'Sócio atualizado com sucesso!')
            return redirect('socios:BuscarSocio')
           
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return redirect('socios:editSocio', id=socio.id)

    else:
        form = SocioForm(instance=socio)
        return render(request, 'admin/socios/edita_socio.html', {'form': form, 'socio': socio})

@login_required
def edit_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    form = SocioForm(request.POST, request.FILES, instance=socio)  # Incluindo request.FILES para lidar com arquivos
    if request.method != 'POST':
        form = SocioForm(instance=socio)
        return render(request, 'admin/socios/edita_socio.html', {'form': form, 'socio': socio})
    if request.method == 'POST':
        if form.is_valid():
            socio = form.save(commit=False)
            socio.nomeCompleto = form.cleaned_data['nomeCompleto']
            socio.cpf = form.cleaned_data['cpf']
            socio.dataNascimento = form.cleaned_data['dataNascimento']
            socio.sexo = form.cleaned_data['sexo']
            socio.registro = form.cleaned_data['registro']
            socio.arq_autoDeclaracao = form.cleaned_data['arq_autoDeclaracao']
            socio.atividade_agr = form.cleaned_data['atividade_agr']
            socio.quantidade_pessoa = form.cleaned_data['quantidade_pessoa']
            socio.cargo = form.cleaned_data['cargo']
            socio.situacao = form.cleaned_data['situacao']
            form.save()
            messages.success(request, 'Sócio atualizado com sucesso!')
            return redirect('socios:BuscarSocio')
           
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            return render(request, 'admin/socios/edita_socio.html', {'form': form, 'socio': socio})
    return render(request, 'admin/socios/edita_socio.html', {'form': form, 'socio': socio})
        

    
@login_required
def delete_socio(request, id):
    """ Deve apenas desativar o sócio e fazer com que ele não apareça mais na lista de sócios """
    socio = get_object_or_404(Socio, id=id)
    socio.situacao = False
    socio.save()
    messages.success(request, 'Sócio desativado com sucesso!')
    return render(request, 'admin/socios/buscar_socios.html', {'socio': socio})

    
    
    
    


def monthly_payment(request):
    monthly_payment = Mensalidade.objects.all()

    return render(request,  "admin/socios/mensalidade.html", {"payment":monthly_payment})