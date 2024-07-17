from django import forms
from .models import Cargo, Socio, Mensalidade


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            'nomeCompleto',
            'cpf','dataNascimento',
            'sexo', 
            'registro',
            'arq_autoDeclaracao',
            'atividade_agr',
            'quantidade_pessoa',
            'cargo',
            'situacao'
        ]

        