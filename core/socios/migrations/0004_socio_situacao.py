# Generated by Django 4.2.11 on 2024-05-10 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0003_rename_socios_socio'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='situacao',
            field=models.BooleanField(default=True, verbose_name='Situação Atual'),
        ),
    ]
