from django.db import models

class RegistroDeInsidentes(models.Model):
    TIPO_INSIDENTE = models.CharField(max_length=30)
    DESCRICAO_INSIDENTE = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.TIPO_INSIDENTE

    class Meta:
        db_table = 'REGISTRO_INSIDENTES'

class Endereco(models.Model):
    CIDADE = models.CharField(max_length=30, primary_key=True, default='Frederico Westphalen')
    BAIRRO = models.CharField(max_length=30)
    RUA = models.CharField(max_length=30)
    NUMERO =models.IntegerField()
    COMPLEMENTO = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.BAIRRO

    class Meta:
        db_table = 'ENDERECO'