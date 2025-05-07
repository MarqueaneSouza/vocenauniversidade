from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Aluno

def lista_alunos(request):
    busca = request.GET.get('busca', '')
    universidade = request.GET.get('universidade', '')

    alunos = Aluno.objects.all()

    if busca:
        alunos = alunos.filter(nome__icontains=busca)

    if universidade:
        alunos = alunos.filter(universidade__icontains=universidade)

    paginator = Paginator(alunos.order_by('nome'), 10)  # 10 alunos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    universidades = Aluno.objects.values_list('universidade', flat=True).distinct()

    return render(request, 'alunos/lista_alunos.html', {
        'page_obj': page_obj,
        'busca': busca,
        'universidade': universidade,
        'universidades': universidades
    })

