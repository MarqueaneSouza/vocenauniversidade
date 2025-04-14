from django.contrib import admin

from .models import Acompanhamento, Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'universidade', 'curso', 'previsao_formatura')
    search_fields = ('nome', 'email', 'cpf')

@admin.register(Acompanhamento)
class AcompanhamentoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'ano', 'periodo')
    search_fields = ('aluno_nome',)
    list_filter = ('ano', 'periodo')