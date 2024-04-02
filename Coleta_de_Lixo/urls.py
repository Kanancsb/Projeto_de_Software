from django.urls import path
from app_Coleta_de_Lixo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Denuncias/Registro_Incidente/', views.registro_incidente, name='registro_incidente'),
]
