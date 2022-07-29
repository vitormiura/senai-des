from django.shortcuts import render, get_object_or_404, redirect
from django.core.validators import validate_email
from home.models import Curso


def home_index(request):
    dados = Curso.objects.all() 
    context={
        'curso' : dados
    }

    return render(request, 'home/index.html', context)

def home_detalhes(request, id):
    #data = Curso.objects.get(id = id)
    data = get_object_or_404(
        Curso, id = id
    )
    return render(request, 'home/detalhes.html', {'curso' : data})

def salvar_curso(request):
    if str(request.method)!='POST':
        return render(request, 'home/form_cadastro.html')
    else:

        nome = request.POST.get('name')
        description = request.POST.get('descriptions')
        active = request.POST.get('active')
        email = request.POST.get('email')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # if (not nome or not description
        #     or not email or not active
        #     or not price):
        #     return redirect(request, 'home/form_cadastro.html')
        
        try:
            validate_email(email)
        except:
            return render(request, 'home/form_cadastro.html')

        if Curso.objects.filter(nome=nome).exists():
            return render(request, 'home/form_cadastro.html')

        data = Curso.objects.create(
            nome = nome,
            description = description,
            active = active,
            email = email,
            price = price,
            image = image,
        )

        data.save()

        #return redirect('homeindex.html')
        return render(request, 'home/index.html')