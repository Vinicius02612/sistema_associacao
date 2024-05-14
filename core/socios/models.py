from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome_cargo = models.CharField(verbose_name="Cargo",max_length=30, blank=True)

    def __str__(self):
        return self.nome_cargo
    
class Socio(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=50, blank=True)
    sobrenome = models.CharField(verbose_name="Sobrenome",max_length=50, blank=True)
    cpf = models.CharField(verbose_name="CPF", max_length=11, blank=True)
    dataNascimento = models.DateField(verbose_name="Data de Nascimento", blank=True)
    sexo = models.CharField(verbose_name="Sexo", max_length=10, blank=True)
    registro = models.CharField(verbose_name="RG", max_length=11, blank=True)
    arq_autoDeclaracao = models.FileField(verbose_name="Auto Declaração",upload_to="declaracoes")
    atividade_agr =  models.CharField(verbose_name="Mantem atividade agricola na comunidade", max_length=4, blank=True)
    quantidade_pessoa = models.IntegerField(verbose_name="Quantidade de pessoas na familia", blank=True)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo", on_delete=models.DO_NOTHING)
    situacao = models.BooleanField(verbose_name="Situação Atual", default=True)
    def __str__(self):
        return self.nome


class Mensalidade(models.Model):
    nome_socio = models.ForeignKey(Socio,on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name="Descrição", max_length=50, blank=True, default="Mensalidade")
    valor = models.FloatField(verbose_name="Valor", blank=True)
    reference_data = models.DateField(verbose_name="Mês de cobrança",blank=True)
    data_validade = models.DateField(verbose_name="Mês de Vencimento", blank=True)
    status = models.BooleanField(verbose_name='Status', default=False)