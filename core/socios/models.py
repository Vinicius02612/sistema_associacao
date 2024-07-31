from django.db import models
from datetime import datetime,timedelta
from validate_docbr import CPF
# Create your models here.
  
class Cargo(models.Model):
    """ Model que representa um cargo """
    nome_cargo = models.CharField(verbose_name="Cargo",max_length=30, blank=False)

    def __str__(self):
        return self.nome_cargo
    
   
class Socio(models.Model):
    """ Model que representa um sócio """
    nomeCompleto = models.CharField(verbose_name="Nome",max_length=50, blank=False)
    cpf = models.CharField(verbose_name="CPF", max_length=11, blank=True)
    dataNascimento = models.DateField(verbose_name="Data de Nascimento", blank=False)
    sexo = models.CharField(verbose_name="Sexo", max_length=10, blank=False,null=False)
    registro = models.CharField(verbose_name="RG", max_length=11, blank=False,null=False)
    arq_autoDeclaracao = models.FileField(verbose_name="Auto Declaração",upload_to="declaracoes/",null=False)
    atividade_agr =  models.CharField(verbose_name="Mantem atividade agricola na comunidade", max_length=4,null=False, blank=False)
    quantidade_pessoa = models.IntegerField(verbose_name="Quantidade de pessoas na familia", blank=False)
    cargo = models.CharField(max_length=50, verbose_name="Cargo", blank=False,null=False)
    situacao = models.BooleanField(verbose_name="Situação Atual",null=False)
    def __str__(self):
        return self.nomeCompleto
    

class Mensalidade(models.Model):
    """ Model que representa a mensalidade de cada sócio """
    nome_socio = models.ForeignKey(Socio,on_delete=models.CASCADE)
    descricao = models.CharField(verbose_name="Descrição", max_length=50, blank=False,null=False, default="Mensalidade")
    valor = models.FloatField(verbose_name="Valor", blank=False,null=False, default=5.00)
    reference_data = models.DateField(verbose_name="Mês de cobrança",blank=False,null=True)
    data_validade = models.DateField(verbose_name="Mês de Vencimento", blank=False, null=True)
    status = models.BooleanField(verbose_name='Status',null=False, default=True)

    """ Sempre que um sócio for cadastrado, uma mensalidade será criada para ele """
    def __str__(self):
        return self.nome_socio.nomeCompleto
    
    def save_monthly_payment(self, *args, **kwargs):
        super(Mensalidade, self).save(*args, **kwargs)

    """ A data de vencimento da mensalidade será sempre 30 dias após a data de cobrança """
    def save_date_validate(self, *args, **kwargs):
         # Define a data de referência da mensalidade
        if not self.reference_data:
            self.reference_data = datetime.now().date()
        # A data de vencimento da mensalidade será sempre 30 dias após a data de cobrança
        self.data_validade = self.reference_data + timedelta(days=30)
        super(Mensalidade, self).save(*args, **kwargs)
    
    """ Data de referencia da mensalidade """
    def save_reference(self, *args, **kwargs):
        self.reference_data = datetime.now()
        super(Mensalidade, self).save(*args, **kwargs)

    """ A mensalidade será sempre de R$ 5,00 """
    def save_value(self, *args, **kwargs):
        self.valor = 5.00
        super(Mensalidade, self).save(*args, **kwargs)
    
    """ O status da mensalidade será sempre ativo """
    def save_status(self, *args, **kwargs):
        self.status = True
        super(Mensalidade, self).save(*args, **kwargs)


class Frequencia(models.Model):
    """ Model que represente uma lista de frequencias de cada sócio, essa deve conter as faltas e presenças de cada sócio durante o ano  """
    nome_socio = models.ForeignKey(Socio,on_delete=models.CASCADE)
    mes = models.CharField(verbose_name="Mês", max_length=20, blank=False,null=False)
    presenca = models.IntegerField(verbose_name="Presença", blank=False,null=False, default=0)
    falta = models.IntegerField(verbose_name="Falta", blank=False,null=False, default=0)
    total = models.IntegerField(verbose_name="Total", blank=False,null=False, default=0)
    def __str__(self):
        return self.nome_socio.nomeCompleto