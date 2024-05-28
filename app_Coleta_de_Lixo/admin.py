from django.contrib import admin
from .models import LinkEndereco, Endereco, RegistroDeInsidentes

@admin.register(LinkEndereco)
class LinkEnderecoAdmin(admin.ModelAdmin):
    list_display = ('ENDERECO_URL', 'NOME_LINK', 'LATITUDE_LINK', 'LONGITUDE_LINK')
    list_display_links = ('ENDERECO_URL',)
    list_editable = ('NOME_LINK', 'LATITUDE_LINK', 'LONGITUDE_LINK')
    search_fields = ('NOME_LINK',)

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('BAIRRO', 'RUA', 'NUMERO')
    search_fields = ('BAIRRO', 'RUA', 'NUMERO')

@admin.register(RegistroDeInsidentes)
class RegistroDeInsidentesAdmin(admin.ModelAdmin):
    list_display = ('TIPO_INSIDENTE', 'DESCRICAO_INSIDENTE', 'get_bairro', 'get_rua', 'get_numero')
    search_fields = ('TIPO_INSIDENTE', 'DESCRICAO_INSIDENTE', 'ENDERECO__BAIRRO', 'ENDERECO__RUA', 'ENDERECO__NUMERO')

    def get_bairro(self, obj):
        return obj.ENDERECO.BAIRRO
    get_bairro.short_description = 'Bairro'
    get_bairro.admin_order_field = 'ENDERECO__BAIRRO'

    def get_rua(self, obj):
        return obj.ENDERECO.RUA
    get_rua.short_description = 'Rua'
    get_rua.admin_order_field = 'ENDERECO__RUA'

    def get_numero(self, obj):
        return obj.ENDERECO.NUMERO
    get_numero.short_description = 'Número'
    get_numero.admin_order_field = 'ENDERECO__NUMERO'