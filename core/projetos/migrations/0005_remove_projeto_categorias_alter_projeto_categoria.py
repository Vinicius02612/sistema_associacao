# Generated by Django 4.2.11 on 2024-05-10 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0004_categorias_projeto_participante_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='categorias',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projetos.categorias', verbose_name='Cargo'),
        ),
    ]
