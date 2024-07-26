from django import forms
from .models import Cargo, Socio, Mensalidade





class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'  # Inclua todos os cam