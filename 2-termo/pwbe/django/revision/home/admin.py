from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'custom_qtd_estoque', 'categoria']

    def custom_qtd_estoque(self, produto):
        if produto.qtd_estoque < 5:
            return 'ESTOQUE BAIXO'
        elif produto.qtd_estoque == 0:
            return 'ZERADO'
        return 'ESTOQUE OK'


admin.site.register(models.Categoria)

@admin.register(models.Cliente)
class AdminCliente(admin.ModelAdmin):
    list_display = ['nome', 'email', 'tipo']
    list_editable = ['tipo']