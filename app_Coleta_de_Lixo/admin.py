from django.contrib import admin
from .models import LinkEndereco

@admin.register(LinkEndereco)
class LinkEnderecoAdmin(admin.ModelAdmin):
    list_display = ('ENDERECO_URL', 'NOME_LINK', 'LATITUDE_LINK', 'LONGITUDE_LINK')
    list_display_links = ('ENDERECO_URL',)
    list_editable = ('NOME_LINK', 'LATITUDE_LINK', 'LONGITUDE_LINK')
    search_fields = ('NOME_LINK',)
