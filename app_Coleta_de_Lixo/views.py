from django.shortcuts import render

def home(request):
    return render(request, 'Denuncias/Registro_de_Insidente.html')