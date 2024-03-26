from app_Coleta_de_Lixo import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home' ),
]
