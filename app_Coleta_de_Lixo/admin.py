from django.contrib import admin
from .models import LinkEndereco

@admin.register(LinkEndereco)
class LinkEnderecoAdmin(admin.ModelAdmin):
    pass

