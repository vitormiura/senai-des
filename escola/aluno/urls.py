from django.urls import path
from . import views

urlpatterns = [
    path('aluno/', views.aluno_index, name = 'aluno_index')
]
