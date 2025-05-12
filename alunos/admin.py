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
        'status',
    )
    list_filter = ('status',)


    @admin.display(description="Admissão")
    def admissao_formatada(self, obj):
        if obj.mes_admissao and obj.ano_admissao:
            return f"{obj.mes_admissao}/{obj.ano_admissao}"
        elif obj.ano_admissao:
            return f"{obj.ano_admissao}"
        return "-"

    @admin.display(description="Formatura")
    def formatura_formatada(self, obj):
        if obj.mes_formatura and obj.ano_formatura:
            return f"{obj.mes_formatura}/{obj.ano_formatura}"
        elif obj.ano_formatura:
            return f"{obj.ano_formatura}"
        return "-"


@admin.register(Acompanhamento)
class AcompanhamentoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'ano', 'periodo', 'rendimento')
    search_fields = ('aluno_nome',)
    list_filter = ('ano', 'periodo')

