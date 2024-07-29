from django.contrib import admin
from .models import Projeto
# Register your models here.




class ProjetosAdmin(admin.ModelAdmin):
    
    list_display = ('id',
                    'titulo',
                    'nome_instituicao',
                    'arquivo_projeto',
                    'cnpj',
                    'data_inicio',
                    'data_final',
                    'categoria',
                    'situacao',
                    )

    list_display_links = ('id','titulo')
    search_fields = ('titulo','nome_instituicao')




admin.site.register(Projeto, ProjetosAdmin)