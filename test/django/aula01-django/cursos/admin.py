from django.contrib import admin
from .models import Cursos

class CursoDisplay(admin.ModelAdmin):
    list_display = ['nome_curso_bosch', 'nome_curso_senai']

admin.site.register(Cursos, CursoDisplay)