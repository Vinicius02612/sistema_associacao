from django.db import models
from socios.models import Socio

class Categorias(models.Model):
    nome = models.CharField(verbose_name="Categoria", max_length=50)
    categoria = "Cimento"

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(verbose_name="Titulo do Projeto", max_length=100, blank=False, null=False)
    nome_instituicao = models.CharField(verbose_name="Nome da instituição", max_length=100, blank=False, null=False)
    arquivo_projeto = models.FileField(verbose_name="Documento do Projeto", upload_to="projetos", null=False)
    data_inicio = models.DateField(verbose_name="Data de início", blank=False, null=False)
    data_final = models.DateField(verbose_name="Data de fim", blank=False, null=False)
    categoria = models.ForeignKey(Categorias, verbose_name="Categoria", on_delete=models.DO_NOTHING)
    participante = models.ForeignKey(Socio, verbose_name="Participante", on_delete=models.DO_NOTHING, blank=False, related_name="projetos")
    situacao = models.BooleanField(verbose_name="Situação atual", blank=False, default=False)

    def __str__(self):
        return self.titulo
