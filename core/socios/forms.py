from django import forms
from .models import  Socio, Mensalidade
from validate_docbr import CPF
from datetime import datetime
# formulario de socios
class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nomeCompleto', 'cpf', 'dataNascimento', 'sexo', 'registro', 'arq_autoDeclaracao', 'atividade_agr', 'quantidade_pessoa', 'cargo', 'situacao']
    
    def __init__(self, *args, **kwargs):
        super(SocioForm, self).__init__(*args, **kwargs)


        self.fields['nomeCompleto'].widget = forms.TextInput(attrs={
            'class': 'form-control  ',
            'id': 'nomeCompleto',
            'placeholder': 'Digite o nome completo'
        })
        self.fields['cpf'].widget = forms.TextInput(attrs={
            'class': 'form-control ',
            'id': 'cpf',
            'placeholder': 'Ex: 000.000.000-00'
        })
        self.fields['sexo'].widget = forms.RadioSelect(attrs={
           
            'class': 'form-check-input ',
        }, choices=[

            ('masculino', 'Masculino'),
            ('feminino', 'Feminino')
        ])
        self.fields['registro'].widget = forms.TextInput(attrs={
            'class': 'form-control ',
            'id': 'registro',
            'placeholder': 'Digite o RG'
        })
        self.fields['arq_autoDeclaracao'].widget = forms.FileInput(attrs={
            'class': 'custom-file-upload ',
            'id': 'arq_autoDeclaracao',
            'style': '',
            'accept': '.pdf',
            'onchange': "document.getElementById('file-name').innerText = this.files[0].name;"
        })
        self.fields['dataNascimento'].widget = forms.DateInput(attrs={
            'class': 'form-control ',
            'id': 'data',
            'type': 'date'
        })
        CHOICES_CARGO=[
            ('', 'Selecione um cargo'),
            ('Associado', 'Associado'),
            ('Secretario', 'Secretario'),
            ('Tesoureiro', 'Tesoureiro'),
            ('1 º Diretor', '1 º Diretor'),
            ('2 º Diretor', '2 º Diretor'),
            ('Fiscais', 'Fiscais'),
            ('Suplentes', 'Suplentes')
        ]
        self.fields['cargo'].widget = forms.Select(attrs={
            'class': 'form-control ',
            'id': 'cargo'
        }, choices=CHOICES_CARGO)
        self.fields['atividade_agr'].widget = forms.Select(attrs={
            'class': 'form-control  ',
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
        self.fields['situacao'].widget = forms.Select(attrs={
                'class': 'form-control ',
                'id': 'situacao'
            }, choices=[
                ('ativo', 'Ativo'),
                ('inativo', 'Inativo')
        ])

  

   
  
    

    