# Generated by Django 5.0.3 on 2024-05-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Coleta_de_Lixo', '0004_linkendereco_nome_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkendereco',
            name='LATITUDE_LINK',
            field=models.FloatField(default=0, max_length=7),
        ),
        migrations.AddField(
            model_name='linkendereco',
            name='LONGITUDE_LINK',
            field=models.FloatField(default=0, max_length=7),
        ),
    ]
