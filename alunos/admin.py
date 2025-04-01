from django.contrib import admin
from .models import Universidade, Curso, Aluno, Rendimento

# personaliza a administração dos modelos Universidade, Curso, Aluno e Rendimento.
# melhora a exibição dos dados no painel administrativo do Django, facilitando buscas e filtros.

@admin.register(Universidade)
class UniversidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado')
    search_fields = ('nome', 'cidade')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'universidade', 'duracao_semestres')
    search_fields = ('nome',)
    list_filter = ('universidade',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'telefone', 'curso', 'universidade', 'data_admissao', 'previsao_formatura', 'ativo')
    search_fields = ('nome', 'cpf', 'email')
    list_filter = ('universidade', 'curso', 'ativo')
    date_hierarchy = 'data_admissao'

@admin.register(Rendimento)
class RendimentoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'ano', 'semestre', 'disciplinas_cursadas', 'disciplinas_aprovadas', 'media_geral')
    search_fields = ('aluno__nome',)
    list_filter = ('ano', 'semestre')
