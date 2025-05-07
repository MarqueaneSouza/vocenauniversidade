from django.contrib import admin

from .models import Acompanhamento, Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'telefone',
        'cpf',
        'email',
        'universidade',
        'curso',
        'admissao_formatada',
        'formatura_formatada',
    )



@admin.register(Acompanhamento)
class AcompanhamentoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'ano', 'periodo', 'rendimento')
    search_fields = ('aluno_nome',)
    list_filter = ('ano', 'periodo')
