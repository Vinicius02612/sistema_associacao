from django import forms
from .models import Cargo, Socio, Mensalidade
from validate_docbr import CPF
from datetime import datetime
# formulario de socios
class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(SocioForm, self).__init__(*args, **kwargs)


        self.fields['nomeCompleto'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'nomeCompleto',
            'placeholder': 'Digite o nome completo'
        })
        self.fields['cpf'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'carteiraTrabalho',
            'placeholder': 'Ex: 000.000.000-00'
        })
        self.fields['sexo'].widget = forms.RadioSelect(attrs={
            'class': 'form-check-input'
        }, choices=[
            ('masculino', 'Masculino'),
            ('feminino', 'Feminino')
        ])
        self.fields['registro'].widget = forms.TextInput(attrs={
            'class': 'form-control RG',
            'id': 'registro',
            'placeholder': 'Digite o RG'
        })
        self.fields['arq_autoDeclaracao'].widget = forms.FileInput(attrs={
            'class': 'custom-file-upload',
            'id': 'arq_autoDeclaracao',
            'style': '',
            'accept': '.pdf',
            'onchange': "document.getElementById('file-name').innerText = this.files[0].name;"
        })
        self.fields['dataNascimento'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'id': 'data'
        })
        self.fields['cargo'].widget = forms.Select(attrs={
            'class': 'form-control',
            'id': 'cargo'
        }, choices=[
            ('', 'Selecione um cargo'),
            ('Associado', 'Associado'),
            ('Secretario', 'Secretario'),
            ('Tesoureiro', 'Tesoureiro'),
            ('1 º Diretor', '1 º Diretor'),
            ('2 º Diretor', '2 º Diretor'),
            ('Fiscais', 'Fiscais'),
            ('Suplentes', 'Suplentes')
        ])
        self.fields['atividade_agr'].widget = forms.Select(attrs={
            'class': 'form-control ',
            'id': 'atividade'
        }, choices=[
            ('sim', 'Sim'),
            ('nao', 'Não')
        ])
        self.fields['quantidade_pessoa'].widget = forms.NumberInput(attrs={
            'class': 'form-control ',
            'id': 'familia',
            'placeholder': 'Digite a quantidade'
        })

    """ Cpdf deve ser valido """
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        _cpf = CPF()
        if  _cpf.validate(cpf) is not True:
            raise forms.ValidationError("CPF inválido")
        return cpf

    """ Verifica se o cargo ja existe, so deve sexistir um cargo com os nomes (Presidente,1º Diretor, 2º Diretor,Suplente, Fiscal , Tesoureiro e Secretario ) """
    def clean_cargo(self):
        cargo = self.cleaned_data['cargo']
        cargos = ['Presidente','1º Diretor','2º Diretor','Suplente','Fiscal','Tesoureiro','Secretario']
        for cargo in cargos:
            if cargo == cargo:
                if Cargo.objects.filter(nome_cargo = cargo).exists():
                    raise forms.ValidationError("Ja existe um sócio com  esse cargo ")
        return cargo
    
    """ Verifica se ja existe um sócio com os dados informados """
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if Socio.objects.filter(cpf = cpf).exists():
            raise forms.ValidationError("Ja existe um sócio com  esses dados ")
        return cpf
    
    """ Verifica se todos os campos foram preenchidos """
    def clean(self):
        cleaned_data = super(SocioForm, self).clean()
        nome = cleaned_data.get('nomeCompleto')
        cpf = cleaned_data.get('cpf')
        sexo = cleaned_data.get('sexo')
        rg = cleaned_data.get('registro')
        declaracao = cleaned_data.get('arq_autoDeclaracao')
        data_nascimento = cleaned_data.get('dataNascimento')
        cargo = cleaned_data.get('cargo')
        atividade = cleaned_data.get('atividade_agr')
        qtdPessoas = cleaned_data.get('quantidade_pessoa')
        if not nome or not cpf or not sexo or not rg or not declaracao or not data_nascimento or not cargo or not atividade or not qtdPessoas:
            raise forms.ValidationError("Todos os campos devem ser preenchidos ")
        return cleaned_data

    """ Verificar validade da  data de Nascimento """
    def clean_dataNascimento(self):
        data_nascimento = self.cleaned_data['dataNascimento']
        if data_nascimento >= datetime.now().date():
            raise forms.ValidationError("Data de nascimento inválida")
        return data_nascimento
    
    """ Quantidade de pessoas deve ser maior ou igual a 0 """
    def clean_quantidade_pessoa(self):
        qtdPessoas = self.cleaned_data['quantidade_pessoa']
        if qtdPessoas < 0:
            raise forms.ValidationError("Quantidade de pessoas deve ser maior ou igual a 0")
        return qtdPessoas
    """ Salvando os dados do sócio """
    def save(self, commit=True):
        instance = super(SocioForm, self).save(commit=False)
        instance.save()
        return instance
  
    

    