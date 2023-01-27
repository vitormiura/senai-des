from django.urls import path
from . import views

urlpatterns = [
    path('aluno_lista/',
         views.aluno_index,
         name='aluno_index'
         ),
    path('aluno_cadastro/',
         views.aluno_cadastro,
         name='aluno_cadastro'
         ),
    path('cadastro_usuario/',
         views.cadastro_usuario,
         name='cadastro_usuario'
         ),
]
