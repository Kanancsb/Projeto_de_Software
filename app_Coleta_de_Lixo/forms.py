from django import forms
from .models import Endereco, LinkEndereco, RegistroDeInsidentes

def validate_numero_casa(value):
    if not value.isdigit():
        raise forms.ValidationError('Apenas números são permitidos para o número da casa.')

class Form_Registro_Insidentes(forms.Form):
    numero_casa = forms.CharField(max_length=5, validators=[validate_numero_casa])

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class LinkEnderecoForm(forms.ModelForm):
    class Meta:
        model = LinkEndereco
        fields = '__all__'

class RegistroDeInsidentesForm(forms.ModelForm):
    class Meta:
        model = RegistroDeInsidentes
        fields = '__all__'