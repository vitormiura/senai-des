from django import forms
from aluno.models import Aluno
from django.contrib.auth.models import User
class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome', 'telefone'
        ]
class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
        ]