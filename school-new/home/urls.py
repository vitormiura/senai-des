from django.urls import path

from . import views

urlpatterns = [
    path('',views.index_home,name='index_home'),
    path('usuario_cadastro/', views.usuario_cadastro, name="usuario_cadastro"),
    path('usuario_login/', views.usuario_login, name="usuario_login"),
    path('sair/', views.sair, name="sair"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
