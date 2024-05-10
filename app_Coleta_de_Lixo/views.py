from django.shortcuts import render, redirect
from .models import RegistroDeInsidentes, Endereco
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import geocoder

def registro_incidente(request):
    if request.method == 'POST':
        tipo_insidente = request.POST.get('Tipo_de_Insidente')
        descricao_insidente = request.POST.get('texto-descricao')

        bairro = request.POST.get('bairro')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero-casa')
        complemento = request.POST.get('complemento')

        registro_insidente = RegistroDeInsidentes.objects.create(TIPO_INSIDENTE=tipo_insidente, DESCRICAO_INSIDENTE=descricao_insidente)
        endereco = Endereco.objects.create(BAIRRO=bairro, RUA=rua, NUMERO=numero ,COMPLEMENTO=complemento)

    return render(request, 'Denuncias/Registro_Incidente.html')

def home(request):

    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    else:
        user_username = request.POST.get('user_username')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')

        user_exist = User.objects.filter(username=user_username).first()

        if user_exist:
            messages.error(request, 'Já existe um usuário com esse nome.')
            return render(request, 'account/signup.html')
        else:
            user = User.objects.create_user(username=user_username, email=user_email, password=user_password, is_staff=True)
            user.save()
            return redirect('login')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')
    else:
        user_username = request.POST.get('user_username')
        user_password = request.POST.get('user_password')

        user_authenticate = authenticate(username=user_username, password=user_password)

        if user_authenticate:
            login(request, user_authenticate)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')