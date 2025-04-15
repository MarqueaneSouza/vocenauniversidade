from django.contrib import admin

from .models import Acompanhamento, Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'curso', 'universidade', 'previsao_formatura') # o que aparece na lista
    search_fields = ('nome', 'cpf', 'email', 'curso', 'universidade') # barra de busca
    list_filter = ('universidade', 'curso', 'previsao_formatura') # filtros do lado direito

@admin.register(Acompanhamento)
class AcompanhamentoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'ano', 'periodo')
    search_fields = ('aluno_nome',)
    list_filter = ('ano', 'periodo')