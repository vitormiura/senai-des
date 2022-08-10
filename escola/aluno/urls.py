from django.urls import path
from . import views

urlpatterns = [
    path('aluno_lista/', views.aluno_index, name = 'aluno_index')
]
