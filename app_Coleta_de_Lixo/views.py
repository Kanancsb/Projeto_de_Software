from django.shortcuts import render
from .models import RegistroDeInsidentes, Endereco

def home(request):
    if request.method == 'POST':
        tipo_insidente = request.POST.get('Tipo_de_Insidente')
        descricao_insidente = request.POST.get('texto-descricao')

        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero-casa')
        complemento = request.POST.get('complemento')

        registro_insidente = RegistroDeInsidentes.objects.create(TIPO_INSIDENTE=tipo_insidente, DESCRICAO_INSIDENTE=descricao_insidente)
        endereco = Endereco.objects.create(BAIRRO=bairro, RUA=rua, NUMERO=numero ,COMPLEMENTO=complemento)

        return render(request, 'Denuncias/Registro_de_Insidente.html')

    return render(request, 'Denuncias/Registro_de_Insidente.html')
