from django.contrib import admin

from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'universidade', 'curso', 'previsao_formatura')
    search_fields = ('nome', 'email', 'cpf')