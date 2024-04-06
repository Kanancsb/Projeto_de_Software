from django.urls import path, include
from app_Coleta_de_Lixo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Denuncias/Registro_Incidente/', views.registro_incidente, name='registro_incidente'),
    path('registration/login', views.login, name='login'),
    path('accounts/', include('allauth.urls')),
]
