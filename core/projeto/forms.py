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
            
        })
        self.fields['nome_instituicao'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'nome_instiuicao',
            
        })
        self.fields['cnpj'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'cnpj',
            
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
        })
        self.fields['data_final'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'id': 'data_final',
            'type': 'date',
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

        if data_inicio and data_final:
            self.check_date(data_inicio, data_final)
        
        
        if self.clean_cnpj(cnpj):
            cleaned_data['cnpj'] = cnpj
        
        if self.clean_arquivo_projeto(arquivo_projeto):
            cleaned_data['arquivo_projeto'] = arquivo_projeto
            

        return cleaned_data
    
    def clean_cnpj(self, cnpj):
        
        __cnpj = CNPJ()
        if not __cnpj.validate(cnpj):
            raise forms.ValidationError('cnpj', 'CNPJ inválido')
        return __cnpj
    
    """ Data final não pode ser menor que a final do projeto """
    def check_date(self, data_inicio, data_final):
        dt_data_inicio = datetime.strptime(str(data_inicio), '%Y-%m-%d').date()
        dt_data_final = datetime.strptime(str(data_final), '%Y-%m-%d').date()

        if dt_data_inicio is not None and dt_data_final is not None:
            if dt_data_final <= dt_data_inicio:
                forms.ValidationError('data_final', 'Data de final não pode ser menor que a inicial')
        
        return [dt_data_inicio, dt_data_final]
    
    """ Arquivo deve ser menor 10mb """
    def clean_arquivo_projeto(self, arquivo_projeto):
        if arquivo_projeto.size > 10000000:
            forms.ValidationError('arquivo_projeto', 'Tamanho do arquivo deve ser menor que 10mb')
        return arquivo_projeto
    
    """ Salvar o projeto no banco de dados """
    def save(self, commit=True):
        projeto = super(FormProjeto, self).save(commit=False)
        if commit:
            projeto.save()
        return projeto