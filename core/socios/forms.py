from django.forms import ModelForm
from .models import Cargo, Socio, Mensalidade
from validate_docbr import CPF
from datetime import datetime
# formulario de socios
class SocioForm(ModelForm):
    class Meta:
        model = Socio
        fields = ['nomeCompleto','cpf','dataNascimento','sexo','registro','arq_autoDeclaracao','atividade_agr','quantidade_pessoa','cargo','situacao']
        
    def clean(self):
        cleaned_data = super(SocioForm, self).clean()
        cpf = cleaned_data.get('cpf')
        _cpf = CPF()
        if  _cpf.validate(cpf) is not True:
            self.add_error('cpf', 'CPF inválido')
        return cleaned_data
    
    def save(self, commit=True):
        instance = super(SocioForm, self).save(commit=False)
        instance.save()
        mensalidade = Mensalidade.objects.create(nome_socio=instance)
        mensalidade.save()
        mensalidade.save_date_validate()
        mensalidade.save_reference()
        mensalidade.save_value()
        mensalidade.save_status()
        return instance
    
    def __init__(self, *args, **kwargs):
        super(SocioForm, self).__init__(*args, **kwargs)
        self.fields['cargo'].queryset = Cargo.objects.all()
        self.fields['dataNascimento'].widget.attrs['type'] = 'date'
        self.fields['arq_autoDeclaracao'].widget.attrs['accept'] = '.pdf'
        self.fields['arq_autoDeclaracao'].widget.attrs['required'] = True
        self.fields['arq_autoDeclaracao'].label = 'Auto Declaração'
        self.fields['atividade_agr'].label = 'Mantem atividade agricola na comunidade'
        self.fields['quantidade_pessoa'].label = 'Quantidade de pessoas na familia'
        self.fields['cargo'].label = 'Cargo'
        self.fields['situacao'].label = 'Situação Atual'
        self.fields['nomeCompleto'].label = 'Nome'
        self.fields['cpf'].label = 'CPF'
        self.fields['dataNascimento'].label = 'Data de Nascimento'
        self.fields['sexo'].label = 'Sexo'
        self.fields['registro'].label = 'RG'
        self.fields['arq_autoDeclaracao'].label = 'Auto Declaração'
        self.fields['atividade_agr'].label = 'Mantem atividade agricola na comunidade'
        self.fields['quantidade_pessoa'].label = 'Quantidade de pessoas na familia'
        self.fields['cargo'].label = 'Cargo'
        self.fields['situacao'].label = 'Situação Atual'
        self.fields['nomeCompleto'].widget.attrs['class'] = 'form-control'
        self.fields['cpf'].widget.attrs['class'] = 'form-control'
        self.fields['dataNascimento'].widget.attrs['class'] = 'form-control'
        self.fields['sexo'].widget.attrs['class'] = 'form-control'
        self.fields['registro'].widget.attrs['class'] = 'form-control'
        self.fields['arq_autoDeclaracao'].widget.attrs['class'] = 'form-control'
        self.fields['atividade_agr'].widget.attrs['class'] = 'form-control'
        self.fields['quantidade_pessoa'].widget.attrs['class'] = 'form-control'
        self.fields['cargo'].widget.attrs['class'] = 'form-control'
        self.fields['situacao'].widget.attrs['class'] = ' form-control'

    

    