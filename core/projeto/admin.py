from django.contrib import admin
from .models import Projeto, Categorias
# Register your models here.



class AdminCategoria(admin.ModelAdmin):
    list_display =('id','nome')

class ProjetosAdmin(admin.ModelAdmin):
    
    list_display = ('id',
                    'titulo',
                    'nome_instituicao',
                    'arquivo_projeto',
                    'data_inicio',
                    'data_final',
                    'categoria',
                    'participante',
                    'situacao',
                    )

    list_display_links = ('id','titulo')
    search_fields = ('titulo','nome_instituicao')



admin.site.register(Categorias, AdminCategoria)
admin.site.register(Projeto, ProjetosAdmin)