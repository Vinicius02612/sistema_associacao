from django.db import models
from socios.models import Socio
# Create your models here.

class Projeto(models.Model):
    titulo = models.CharField(verbose_name="Titulo do Projeto", max_length=100, blank=False, null=False)
    nome_instituicao = models.CharField(verbose_name="Nome da instituicao", max_length=100, blank=False, null=False)
    cnpj = models.CharField(verbose_name="CNPJ",blank=False, max_length=14)
    arquivo_projeto = models.FileField(verbose_name="Documento do Projeto", upload_to="./projetos", null=False)
    data_inicio = models.DateField(verbose_name="Data de inicio", blank=True,null=True)
    data_final = models.DateField(verbose_name="Data de inicio", blank=True, null=True)
    CATEGORIA_CHOICES = [
        ('Esportes', 'Esportes'),
        ('Educacao', 'Educação'),
        ('Cultura', 'Cultura'),
        ('Pesquisa', 'Pesquisa'),
        ('Projeto Social', 'Projeto Social'),
        ('Musica', 'Música'),
        ('Arte', 'Arte'),
    ]
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, blank=False, null=False)
    situacao = models.BooleanField(verbose_name="Situação atual",blank=False, default=False)


    def __str__(self):
        return self.titulo
    