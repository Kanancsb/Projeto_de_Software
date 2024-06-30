from django.shortcuts import render, redirect
from .models import RegistroDeInsidentes, Endereco, LinkEndereco
from .forms import EnderecoForm, LinkEnderecoForm, RegistroDeInsidentesForm
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
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        endereco = Endereco.objects.create(
            BAIRRO=bairro,
            RUA=rua,
            NUMERO=numero,
            COMPLEMENTO=complemento)

        LinkEndereco.objects.create(
            ENDERECO_URL="",
            NOME_LINK="",
            LATITUDE_LINK=latitude,
            LONGITUDE_LINK=longitude,
            RESOLVIDO_LINK=True)

        RegistroDeInsidentes.objects.create(
            TIPO_INSIDENTE=tipo_insidente,
            DESCRICAO_INSIDENTE=descricao_insidente,
            ENDERECO=endereco
        )

    return render(request, 'Denuncias/Registro_Incidente.html')

def home(request):
    ultimos_links = LinkEndereco.objects.filter(RESOLVIDO_LINK=False).order_by('-COD_LINK')

    if ultimos_links.exists():
        last_link = ultimos_links.first()  # Obter o primeiro link não resolvido, não o último global

        if last_link is not None:
            latitude = last_link.LATITUDE_LINK
            longitude = last_link.LONGITUDE_LINK
        else:
            latitude = -27.35917
            longitude = -53.39444

        context = {
            'latitude': latitude,
            'longitude': longitude,
            'token': 'pk.eyJ1Ijoia2FuYW4xMjMiLCJhIjoiY2x2bGVxc2Z5MmEyODJycGh4czFwbnhzNSJ9.QLx0-ruC1MtD8BQfZl5_7A',
            'map_style': 'mapbox://styles/mapbox/streets-v11',
            'zoom': 15,
            'center': [longitude, latitude],
            'interactive': True,
            'ultimos_links': ultimos_links
        }
    else:
        context = {
            'latitude': -27.35917,
            'longitude': -53.39444,
            'token': 'pk.eyJ1Ijoia2FuYW4xMjMiLCJhIjoiY2x2bGVxc2Z5MmEyODJycGh4czFwbnhzNSJ9.QLx0-ruC1MtD8BQfZl5_7A',
            'map_style': 'mapbox://styles/mapbox/streets-v11',
            'zoom': 15,
            'center': [-53.39444, -27.35917],
            'interactive': True,
            'ultimos_links': []
        }

    return render(request, 'Home.html', context)


def signup(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    else:
        user_username = request.POST.get('user_username')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        confirm_password = request.POST.get('confirm_password')

        if not user_username or not user_email or not user_password or not confirm_password:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'account/signup.html')

        if user_password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'account/signup.html')

        user_exist = User.objects.filter(username=user_username).first()

        if user_exist:
            messages.error(request, 'Já existe um usuário com esse nome.')
            return render(request, 'account/signup.html')

        user_exist_email = User.objects.filter(email=user_email).first()

        if user_exist_email:
            messages.error(request, 'Já existe um usuário com esse e-mail.')
            return render(request, 'account/signup.html')

        user = User.objects.create_superuser(username=user_username, email=user_email, password=user_password, is_staff=True)
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


def admin_view(request):
    enderecos = Endereco.objects.all()
    registros = RegistroDeInsidentes.objects.all()
    links = LinkEndereco.objects.all()

    if request.method == 'POST':
        endereco_id = request.POST.get('endereco_id')
        if endereco_id:
            rua = request.POST.get('rua')
            numero = request.POST.get('numero')
            bairro = request.POST.get('bairro')

            endereco = Endereco.objects.get(pk=endereco_id)
            endereco.RUA = rua
            endereco.NUMERO = numero
            endereco.BAIRRO = bairro
            endereco.save()

        registro_id = request.POST.get('registro_id')
        if registro_id:
            tipo_incidente = request.POST.get('tipo_incidente')
            descricao_incidente = request.POST.get('descricao_incidente')

            registro = RegistroDeInsidentes.objects.get(pk=registro_id)
            registro.TIPO_INSIDENTE = tipo_incidente
            registro.DESCRICAO_INSIDENTE = descricao_incidente
            registro.save()

        link_id = request.POST.get('link_id')
        if link_id:
            endereco_url = request.POST.get('endereco_url')
            nome_link = request.POST.get('nome_link')
            latitude_link = request.POST.get('latitude_link').replace(',', '.')
            longitude_link = request.POST.get('longitude_link').replace(',', '.')
            resolvido_link = request.POST.get('resolvido_link')

            if resolvido_link == 'on':
                resolvido_link = True
            else:
                resolvido_link = False

            link = LinkEndereco.objects.get(pk=link_id)
            link.ENDERECO_URL = endereco_url
            link.NOME_LINK = nome_link
            link.LATITUDE_LINK = float(latitude_link)
            link.LONGITUDE_LINK = float(longitude_link)
            link.RESOLVIDO_LINK = resolvido_link
            link.save()

        return redirect('admin_index')

    context = {
        'enderecos': enderecos,
        'registros': registros,
        'links': links,
    }

    return render(request, 'admin_pages/admin_index.html', context)