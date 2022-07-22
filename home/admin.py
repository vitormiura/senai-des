from django.contrib import admin

from home.models import Agenda

class detailAgenda(admin.ModelAdmin):
    list_display =  ('id','name', 'date', 'is_active')
    list_editable = ('is_active',)
    list_per_page = 15
    search_fields = ('name',)
    list_display_links = ('name',)

admin.site.register(Agenda, detailAgenda)
