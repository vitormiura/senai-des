from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_index, name = 'homeindex'),
    path('detalhes/<int:id>', views.home_detalhes, name = 'homedetalhes'),
    path('salvar_curso/', views.salvar_curso, name = 'salvar_curso'),
]
