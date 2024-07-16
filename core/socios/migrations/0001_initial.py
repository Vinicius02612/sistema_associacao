# Generated by Django 4.2.13 on 2024-07-15 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cargo', models.CharField(max_length=30, verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(blank=True, max_length=11, verbose_name='CPF')),
                ('dataNascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(max_length=10, verbose_name='Sexo')),
                ('registro', models.CharField(max_length=11, verbose_name='RG')),
                ('arq_autoDeclaracao', models.FileField(upload_to='declaracoes', verbose_name='Auto Declaração')),
                ('atividade_agr', models.CharField(max_length=4, verbose_name='Mantem atividade agricola na comunidade')),
                ('quantidade_pessoa', models.IntegerField(verbose_name='Quantidade de pessoas na familia')),
                ('situacao', models.BooleanField(default=True, verbose_name='Situação Atual')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='socios.cargo', verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Mensalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='Mensalidade', max_length=50, verbose_name='Descrição')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('reference_data', models.DateField(verbose_name='Mês de cobrança')),
                ('data_validade', models.DateField(default=False, verbose_name='Mês de Vencimento')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('nome_socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socios.socio')),
            ],
        ),
    ]
