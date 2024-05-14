# Generated by Django 4.2.11 on 2024-05-08 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100, verbose_name='Titulo do Projeto')),
                ('nome_instituicao', models.CharField(blank=True, max_length=100, verbose_name='Nome da instituicao')),
                ('arquivo_projeto', models.FileField(upload_to='projetos', verbose_name='Documento do Projeto')),
                ('data_inicio', models.DateField(blank=True, verbose_name='Data de inicio')),
                ('data_final', models.DateField(verbose_name='Data de inicio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projetos.categoria', verbose_name='Cargo')),
            ],
        ),
       
    ]
