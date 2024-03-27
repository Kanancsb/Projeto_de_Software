from django import forms

class Form_Registro_Insidentes(forms.Form):
    numero_casa = forms.CharField(max_length=5, validators=[validate_numero_casa])

def validate_numero_casa(value):
    if not value.isdigit():
        raise forms.ValidationError('Apenas números são permitidos para o número da casa.')