# Generated by Django 4.2.14 on 2024-07-29 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0006_alter_projeto_categoria_delete_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='cnpj',
            field=models.CharField(max_length=14, verbose_name='CNPJ'),
        ),
    ]
