from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Denuncias/Registro_Incidente/', views.registro_incidente, name='registro_incidente'),
    path('account/signup', views.signup, name='signup'),
    path('account/login', views.login_view, name='login'),
    path('account/logout', views.logout_view, name='logout')
]
