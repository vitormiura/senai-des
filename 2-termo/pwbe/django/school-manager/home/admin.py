from encodings import search_function
from django.contrib import admin
from home.models import Curso   

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email','active')
    list_editable = ('active',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 15

admin.site.register(Curso, CursoAdmin)