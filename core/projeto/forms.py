from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'nome_instituicao', 'arquivo_projeto', 'data_inicio', 'data_final', 'categoria', 'participante', 'situacao']
