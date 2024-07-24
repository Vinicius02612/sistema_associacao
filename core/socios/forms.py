from django.forms import ModelForm
from django import forms
from .models import Cargo, Socio, Mensalidade
from validate_docbr import CPF
from datetime import datetime
# formulario de socios
class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        
  
    

    