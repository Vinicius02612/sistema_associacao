from django import forms
from .models import Cargo, Socio, Mensalidade

# formulario de socios
class SocioForm(forms.Form):
    class Meta:
        model = Socio
        fields = [
            'nomeCompleto',
            'cpf',
            'dataNascimento',
            'sexo', 
            'registro',
            'arq_autoDeclaracao',
            'atividade_agr',
            'quantidade_pessoa',
            'cargo',
            'situacao'
        ]

    nomeCompleto = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'})
    )
    cpf = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 000.000.000-00'})
    )
    
    atividade_agr = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa', 'type': 'date'})
    )
    sexo = forms.ChoiceField(
        choices=[('M', 'Masculino'), ('F', 'Feminino')],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    registro = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o RG'})
    )
    arq_autoDeclaracao = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control-file'})
    )

    cargo = forms.CharField(
        max_length=100,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    activity = forms.ChoiceField(
        choices=[('yes', 'Sim'), ('no', 'Não')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    quantidade_pessoa = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade'})
    )

