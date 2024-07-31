from django.contrib import admin
from .models import Socio, Cargo, Mensalidade, Frequencia
# Register your models here.

class AdminCargo(admin.ModelAdmin):
    list_display = ('id','nome_cargo')
class SociosAdmin(admin.ModelAdmin):
    
    list_display = ('id',
                    'nomeCompleto',
                    'cpf',
                    'dataNascimento',
                    'sexo',
                    'registro',
                    'arq_autoDeclaracao',
                    'atividade_agr',
                    'quantidade_pessoa',
                    'cargo',
                    'situacao',
                    )

    list_display_links = ('id',)
    search_fields = ('nome','cpf',)
    list_editable = ('nomeCompleto',
                    'cpf',
                    'dataNascimento',
                    'sexo',
                    'registro',
                    'arq_autoDeclaracao',
                    'atividade_agr',
                    'quantidade_pessoa',
                    'cargo',
                    'situacao',
                )


class AdminMensalidade(admin.ModelAdmin):
    list_display = ('id', 'nome_socio', 'descricao','reference_data', 'data_validade','status')


class AdminFrequencia(admin.ModelAdmin):
    list_display = ('id', 'nome_socio','mes','presenca','falta','total')
    list_display_links = ('id', 'nome_socio','mes','presenca','falta','total')

admin.site.register(Cargo,AdminCargo)
admin.site.register(Socio, SociosAdmin)
admin.site.register(Mensalidade, AdminMensalidade)
admin.site.register(Frequencia, AdminFrequencia)