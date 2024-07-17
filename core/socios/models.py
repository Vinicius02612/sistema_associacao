from django.db import models

# Create your models here.

class Cargo(models.Model):
    nome_cargo = models.CharField(verbose_name="Cargo",max_length=30, blank=False)

    def __str__(self):
        return self.nome_cargo
    
class Socio(models.Model):
    nomeCompleto = models.CharField(verbose_name="Nome",max_length=50, blank=False)
    cpf = models.CharField(verbose_name="CPF", max_length=11, blank=True)
    dataNascimento = models.DateField(verbose_name="Data de Nascimento", blank=False)
    sexo = models.CharField(verbose_name="Sexo", max_length=10, blank=False,null=False)
    registro = models.CharField(verbose_name="RG", max_length=11, blank=False,null=False)
    arq_autoDeclaracao = models.FileField(verbose_name="Auto Declaração",upload_to="declaracoes",null=False)
    atividade_agr =  models.CharField(verbose_name="Mantem atividade agricola na comunidade", max_length=4,null=False, blank=False)
    quantidade_pessoa = models.IntegerField(verbose_name="Quantidade de pessoas na familia", blank=False)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo", on_delete=models.DO_NOTHING,null=False)
    situacao = models.BooleanField(verbose_name="Situação Atual", default=True,null=False)
    def __str__(self):
        return self.nomeCompleto


class Mensalidade(models.Model):
    nome_socio = models.ForeignKey(Socio,on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name="Descrição", max_length=50, blank=False,null=False, default="Mensalidade")
    valor = models.FloatField(verbose_name="Valor", blank=False,null=False)
    reference_data = models.DateField(verbose_name="Mês de cobrança",blank=False,null=False)
    data_validade = models.DateField(verbose_name="Mês de Vencimento",default=False, blank=False,null=False)
    status = models.BooleanField(verbose_name='Status', default=False,null=False)