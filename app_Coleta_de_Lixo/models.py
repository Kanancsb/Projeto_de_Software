from django.db import models

class RegistroDeInsidentes(models.Model):
    COD_REGISTRO = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    TIPO_INSIDENTE = models.CharField(max_length=30)
    DESCRICAO_INSIDENTE = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.TIPO_INSIDENTE

    class Meta:
        db_table = 'REGISTRO_INSIDENTES'

class Endereco(models.Model):
    COD_ENDERECO = models.AutoField(primary_key=True)
    CIDADE = models.CharField(max_length=30, default='Frederico Westphalen')
    BAIRRO = models.CharField(max_length=30)
    RUA = models.CharField(max_length=30)
    NUMERO =models.CharField(max_length=5, null=True)
    COMPLEMENTO = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.CIDADE

    class Meta:
        db_table = 'ENDERECO'

class LinkEndereco(models.Model):
    COD_LINK = models.AutoField(primary_key=True)
    ENDERECO_URL = models.URLField(null=False, max_length=200)
    NOME_LINK = models.CharField(null=True, max_length=50)
    def __str__(self):
        return self.ENDERECO_URL

    class Meta:
        db_table = 'LINK_ENDERECO'