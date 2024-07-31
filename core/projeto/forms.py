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
       
    """ Criar todas das validações dos campos do formulario de projeto """
    def clean(self):
        cleaned_data = super(FormProjeto, self).clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_final = cleaned_data.get('data_final')
        cnpj = cleaned_data.get('cnpj')
        arquivo_projeto = self.cleaned_data.get('arquivo_projeto')
        titulo = cleaned_data.get('titulo')
        nome_instituicao = cleaned_data.get('nome_instituicao')
        situacao = cleaned_data.get('situacao')
        __cnpj = CNPJ()
 
        """ verifica se todos os campos  do formulario estão preenchidos """
        if not titulo and not nome_instituicao and not situacao and not data_final and not data_final and not cnpj and not arquivo_projeto:
            self.add_error('titulo', 'Titulo é obrigatório')
            self.add_error('nome_instituicao', 'Nome da instituição é obrigatório')
            self.add_error('situacao', 'Situação é obrigatória')
            self.add_error('data_final', 'Data final é obrigatória')
            self.add_error('data_inicio', 'Data de inicio é obrigatória')
            self.add_error('cnpj', 'CNPJ é obrigatório')
            self.add_error('arquivo_projeto', 'Arquivo do projeto é obrigatório')

        if situacao == 'ativo':
            cleaned_data['situacao'] = True
        if situacao == 'inativo':
            cleaned_data['situacao'] = False

        if not data_final and not data_inicio:
            self.add_error('data_final', 'Data final é obrigatória')
            self.add_error('data_inicio', 'Data de inicio é obrigatória')
            

        """ Validação para verificar se a data final é maior que a data de inicio """
        if data_inicio and data_final:
            if data_final <= data_inicio:
                self.add_error('data_final', 'Data final deve ser maior que a data de inicio')
        
        """ Vvalidação para verificar se o CNPJ é valido """
        if cnpj:
            if not __cnpj.validate(cnpj):
                self.add_error('cnpj', 'CNPJ inválido')
        
        """ Vvalidação para verificar se o arquivo é um pdf """
        if arquivo_projeto:
            if not arquivo_projeto.name.endswith('.pdf'):
                self.add_error('arquivo_projeto', 'O arquivo deve ser um PDF')

        return cleaned_data
       
        

        



   