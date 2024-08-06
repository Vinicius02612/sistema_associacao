from django import forms
from django import forms
from .models import Projeto
from validate_docbr import CNPJ
from datetime import datetime


class FormProjeto(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(FormProjeto, self).__init__(*args, **kwargs)


        self.fields['titulo'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'titulo',
            'placeholder': 'Titulo do projeto'
            
        })
        self.fields['nome_instituicao'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'nome_instiuicao',
            'placeholder': 'Nome da instituição'
        })
        self.fields['cnpj'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'cnpj',
            'placeholder': 'informe o CNPJ',
            
        })

        self.fields['arquivo_projeto'].widget = forms.FileInput(attrs={
            'class': 'custom-file-upload',
            'id': 'arquivo_projeto',
            'style': '',
            'accept': '.pdf',
            'onchange': "document.getElementById('file-name').innerText = this.files[0].name;"
        })
        self.fields['data_inicio'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'id': 'data_inicio',
            'type': 'date',
            'placeholder': 'Data de inicio'
        })
        self.fields['data_final'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'id': 'data_final',
            'type': 'date',
            'placeholder': 'Data final'
        })

        CATEGORIA_CHOICES = [
            ('Esportes', 'Esportes'),
            ('Educacao', 'Educação'),
            ('Cultura', 'Cultura'),
            ('Pesquisa', 'Pesquisa'),
            ('Projeto Social', 'Projeto Social'),
            ('Musica', 'Música'),
            ('Arte', 'Arte'),
        ]
        self.fields['categoria'].widget = forms.Select(attrs={
            'class': 'form-control',
            'id': 'categoria'
        }, choices=CATEGORIA_CHOICES)
        self.fields['situacao'].widget = forms.Select(attrs={
            'class': 'form-control ',
            'id': 'situacao'
        }, choices=[
            ('ativo', 'Ativo'),
            ('inativo', 'Inativo')
        ])

    def clean_situacao(self):
        situacao = self.cleaned_data['situacao']
        if situacao == 'ativo':
            return True
        else:
            return False
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        _cnpj = CNPJ()
        if _cnpj.validate(cnpj) is not True:
            raise forms.ValidationError("CNPJ inválido")
        return cnpj
    
    def clean_data_inicio(self):
        data = self.cleaned_data['data_inicio']
        if data < datetime.now().date():
            raise forms.ValidationError("Data de início inválida")
        return data
       
    
    def clean_data_final(self):
        data = self.cleaned_data['data_final']
        if data < datetime.now().date():
            raise forms.ValidationError("Data final inválida")
        return data
    
    