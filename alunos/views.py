from django.shortcuts import render

from alunos.models import Aluno, Acompanhamento

def painel_acompanhamento(request):
    acompanhamentos = Acompanhamento.objects.select_related('aluno').all()
    return render(request, 'aluno/painel.html', {'acompanhamentos': acompanhamentos})
    
