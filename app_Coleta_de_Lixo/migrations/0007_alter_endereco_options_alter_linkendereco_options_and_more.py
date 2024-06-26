# Generated by Django 5.0.3 on 2024-06-18 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Coleta_de_Lixo', '0006_registrodeinsidentes_endereco'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='endereco',
            options={'verbose_name': 'Endereço', 'verbose_name_plural': 'Endereços'},
        ),
        migrations.AlterModelOptions(
            name='linkendereco',
            options={'verbose_name': 'Link de Endereço', 'verbose_name_plural': 'Links de Endereços'},
        ),
        migrations.AlterModelOptions(
            name='registrodeinsidentes',
            options={'verbose_name': 'Registro de Incidente', 'verbose_name_plural': 'Registros de Incidentes'},
        ),
        migrations.AddField(
            model_name='linkendereco',
            name='RESOLVIDO_LINK',
            field=models.BooleanField(default=False),
        ),
    ]
