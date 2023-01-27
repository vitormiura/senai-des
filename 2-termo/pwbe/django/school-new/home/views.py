from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def index_home(request):
    return render(request, 'home/index.html')

def usuario_cadastro(request):
    if str(request.method)=='POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        primeiro = request.POST.get('primeiro')
        senha1 = request.POST.get('senha1')
        senha2 = request.POST.get('senha2')

        try:
            validate_email(email)

        except:
            messages.error(request, 'not valid email')
            return render(request, 'home/cadastro.html')

        if len(senha1) < 6:
            messages.error(request, 'password must contain at least 6 digits')
            return render(request, 'home/cadastro.html')
        
        if senha1 != senha2:
            messages.error(request, 'senhas diff')
            return render(request, 'home/cadastro.html')
        
        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuario ja existe')
            return render(request, 'home/cadastro.html')

        novo_usuario = User.objects.create_user(
            username = usuario,
            first_name = primeiro,
            email = email,
            password = senha1,
        )
        novo_usuario.save()
        messages.success(request, 'salvo')
        return render(request, 'home/cadastro.html')
    else:
        return render(request, 'home/cadastro.html')

    return render(request, 'home/cadastro.html')

def usuario_login(request):
    if str(request.method) != 'POST':
        return render(request, 'home/login.html')
    else:
        usuario = request.POST.get('login')
        senha = request.POST.get('senha')

        user_login = auth.authenticate(
            username = usuario,
            password = senha
        )
        if user_login:
            auth.login(request, user_login)
            return render(request, 'home/dashboard.html')
        else:
            messages.warning(request, 'credenciais invalidas!')
            return render(request, 'home/login.html')
    
    return render(request, 'home/login.html')

def sair(request):
    auth.logout(request)
    return render(request, 'home/login.html')

@login_required(redirect_field_name='usuario_login')
def dashboard(request):
    return render(request, 'home/login.html')